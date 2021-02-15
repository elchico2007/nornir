from nornir import InitNornir
from nornir.core.task import Task, Result

nr = InitNornir(config_file="config.yaml")

def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world!"
    )
result = nr.run(task=hello_world)

