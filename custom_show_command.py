from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_cli

def custom_show_command(task: Task, text: str) -> Result:
    '''
    Function to run custom command
    '''
    output = task.run(
        task=napalm_cli, commands=[text],
        name="Running custom show command"
    )
    return Result(
        host=task.host,
        result=output
    )

nr = InitNornir(config_file="config.yaml")

# run only against eos
device_eos = nr.filter(F(platform="eos"))

show_command = input("What show command would you like to run on EOS? ")

# run the following command
result = device_eos.run(
    name="Running show command",
    task=custom_show_command,
    text=show_command
)

print_result(result)
