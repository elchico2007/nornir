from nornir import InitNornir
from nornir.core.filter import F
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_cli

nr = InitNornir(config_file="config.yaml")
# run only against junos or eos
devices_junos_eos = nr.filter(F(platform="junos") | F(platform="eos"))

# run the following command
result = devices_junos_eos.run(napalm_cli, commands=['show version'])

print_result(result)
