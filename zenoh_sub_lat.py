import sys
import time
import argparse
import json
import zenoh
from zenoh import config, CongestionControl, Value

# --- Command line argument parsing --- --- --- --- --- ---
parser = argparse.ArgumentParser(
    prog='z_pub_thr',
    description='zenoh throughput pub example')
parser.add_argument('--mode', '-m', dest='mode',
                    choices=['peer', 'client'],
                    type=str,
                    help='The zenoh session mode.')
parser.add_argument('--connect', '-e', dest='connect',
                    metavar='ENDPOINT',
                    action='append',
                    type=str,
                    help='Endpoints to connect to.')
parser.add_argument('--listen', '-l', dest='listen',
                    metavar='ENDPOINT',
                    action='append',
                    type=str,
                    help='Endpoints to listen on.')
parser.add_argument('--samples', '-n',
                    type = int,
                    default=100, 
                    help='The no. of roundtrips to measure.')
parser.add_argument('--warmup', '-w',
                    type = int,
                    default=1, 
                    help='The no. of seconds to warmup.')
parser.add_argument('payload_size',
                    type=int,
                    help='Sets the size of the payload to publish.')
parser.add_argument('--config', '-c', dest='config',
                    metavar='FILE',
                    type=str,
                    help='A configuration file.')

args = parser.parse_args()
conf = zenoh.Config.from_file(args.config) if args.config is not None else zenoh.Config()
if args.mode is not None:
    conf.insert_json5(zenoh.config.MODE_KEY, json.dumps(args.mode))
if args.connect is not None:
    conf.insert_json5(zenoh.config.CONNECT_KEY, json.dumps(args.connect))
if args.listen is not None:
    conf.insert_json5(zenoh.config.LISTEN_KEY, json.dumps(args.listen))
duration = args.warmup
n = args.samples
size=args.payload_size

data = bytearray()
for i in range(0, size):
    data.append(i%10)
data = Value(bytes(data))

def exit_code():
    print('Done')
zenoh.init_logger()

session = zenoh.open(conf)
receiver = session.declare_subscriber("test/pong", exit_code)
subscriber=zenoh.Subscriber(receiver)
publisher = session.declare_publisher('test/ping', congestion_control=CongestionControl.BLOCK())

samples = []
print('Warming up')
now = time.time()
while (time.time()-now) < duration:
    data1 = data
    data = data1
    publisher.put(data)
    _ = subscriber.s

for _ in range(0, n):
    data1 = data
    data = data1
    write_time = time.time()
    publisher.put(data)
    _ = subscriber.s()
    ts = (time.time()-write_time)*1e6
    samples.append(ts)

i = 0
for rtt in samples:
    print(f'{0} bytes : seq = {1} rr={2}microsec, latency = {3}microsec'.format(size, i, rtt, rtt/2))
    i+=1