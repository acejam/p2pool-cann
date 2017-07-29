from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(

 cannabiscoin=math.Object(
        PARENT=networks.nets['cannabiscoin'],
        SHARE_PERIOD=7,
        NEW_SHARE_PERIOD=7,
        CHAIN_LENGTH=24*60*60//10,
        REAL_CHAIN_LENGTH=24*60*60//10,
        TARGET_LOOKBEHIND=200,
        SPREAD=30,
        NEW_SPREAD=30,
        IDENTIFIER='1bfe14c3cc75a0c9'.decode('hex'),
        PREFIX='1bfe14c3cd0e374a'.decode('hex'),
        P2P_PORT=28742,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=28741,
        BOOTSTRAP_ADDRS='crypto.office-on-the.net p2p-spb.xyz'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-cann',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
