#!bin/python
import sys
import time

import nuka
from nuka.tasks import shell
from nuka.hosts import Host
from nuka.process import asyncssh_connections


nuka.cli.add_argument('-n', metavar='N', type=int, default=0)
nuka.cli.add_argument('-t', '--timeout', metavar='N', type=int, default=30)

args, _ = nuka.cli.parse_known_args()

nuka.config['ssh']['extra_options'] = [
    '-oStrictHostKeyChecking=no',
    '-oConnectionAttempts=3',
    '-oConnectTimeout=%s' % args.timeout
]

nuka.cli.parse_args()


async def run_client(host):
    etc = await shell.command(['ls', '/etc'])
    return (host, etc)


names = [h.strip() for h in sys.stdin.readlines() if h.strip()]

if nuka.cli.args.n:
    names = names[:nuka.cli.args.n]

hosts = []
for name in names:
    if name.split('.')[0].isdigit():
        hosts.append(Host(address=name))
    else:
        hosts.append(Host(name))

start = time.time()
results = nuka.run(*[run_client(h) for h in hosts])
print('\nGot {0} valid results for {1} hosts in {2:.02f}s\n\n'.format(
    len([r for r in results if not isinstance(r, Exception)]),
    len(results), time.time() - start)
)

fmt = '{0:10}{1:>10}{2:>10}{3:>10}{4:>10}'
print(fmt.format('', 'min', 'max', 'avg', 'count'))

fmt = '{0:10}{1:10.6f}{2:10.6f}{3:10.6f}{4:10.0f}'
for key in ('connect', 'auth_time', 'timeouts'):
    values = []
    for d in asyncssh_connections.values():
        if isinstance(d, dict):
            if key in d:
                values.append(d[key])
    print(fmt.format(key, min(values), max(values),
                     sum(values) / len(values), len(values)))
