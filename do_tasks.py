#!bin/python
import nuka
from nuka.hosts import DockerContainer

from tasks import mytask


async def do_tasks(host):
    res = await mytask()
    print(res.stdout)

nuka.run(do_tasks(DockerContainer('pyconfr')))
