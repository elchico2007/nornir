from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

# Setting function to take in text
def get_facts(task: Task) -> Result:
    facts = task.run(
        task=napalm_get, getters=['facts']
    )
    return Result(
        host=task.host,
        result=facts
    )

nr = InitNornir(config_file="config.yaml")

# run only against junos or eos
devices_junos_eos = nr.filter(F(platform="junos") | F(platform="eos"))

result = devices_junos_eos.run(
    name="Gathering users from device",
    task=get_facts
)

print_result(result)

# Printing a single hosts serial number
print(result['lab-dcs-1'][1].result['facts']['serial_number'])