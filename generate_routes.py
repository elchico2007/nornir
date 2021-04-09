from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_configure
from jsonrpclib import Server
import ssl
import random

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

def generate_routes(task: Task) -> Result:

    switch = Server(f"https://{task.host.username}:{task.host.password}@{task.host.hostname}/command-api")


    # generating vlans first
    for iter in range(300, 801):
        switch.runCmds(1, [ 
            "enable",
            "configure",
            f"vlan {iter}", 
            f"name VLAN_FOR_{iter}",
            f"interface vlan {iter}",
            f"ip address {random.choice(['10', '192', '172' ])}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}/{random.choice(['31', '24', '32'])}"        ])

    return Result(
        host=task.host,
        result="Configured Routes!",
        changed=True
    )

nr = InitNornir(config_file="config.yaml")

eos_only = nr.filter(F(platform="eos"))

result = eos_only.run(
    name="Geenerating Routes",
    task=generate_routes
    )

print_result(result)