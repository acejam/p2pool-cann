import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc
from operator import *


@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)


@defer.inlineCallbacks
def get_subsidy(bitcoind, target):
    res = yield bitcoind.rpc_getblock(target)

    defer.returnValue(res)

nets = dict(

cannabiscoin=math.Object(
        P2P_PREFIX='fec3b9de'.decode('hex'),
        P2P_PORT=39348,
        ADDRESS_VERSION=28,
        RPC_PORT=39347,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'CannabisCoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda bitcoind, target: get_subsidy(bitcoind, target),
        BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('x11_hash').getPoWHash(data)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('x11_hash').getPoWHash(data)),
        BLOCK_PERIOD=42,
        SYMBOL='CANN',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'CannabisCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/CannabisCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.CannabisCoin'), 'CannabisCoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='https://chainz.cryptoid.info/cann/block.dws?',
        ADDRESS_EXPLORER_URL_PREFIX='https://chainz.cryptoid.info/cann/address.dws?',
        TX_EXPLORER_URL_PREFIX='https://chainz.cryptoid.info/cann/tx.dws?',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
