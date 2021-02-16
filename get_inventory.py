from nornir import InitNornir
from nornir.core.inventory import Host
import json

nr = InitNornir(config_file="config.yaml")

# prints the schema designed for hosts file and groups file
print(json.dumps(Host.schema(), indent=4))

# prints hosts
print(nr.inventory.hosts.keys())

# prints groups
print(nr.inventory.groups)

# inheritence
lab_vdx_1 = nr.inventory.hosts['lab-vdx-1']

# printing domain from global
print(lab_vdx_1['domain'])

# printing domain from local group
print(lab_vdx_1['asn'])

