from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def say(task: Task, text: str) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host} says {text}"
    )
result = nr.run(
    name="Saying goodbye in a friendly manner",
    task=say,
    text="goodbye!")

print_result(result)
