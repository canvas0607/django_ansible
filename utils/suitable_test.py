from suitable import Api
import json


api = Api(
    '183.61.128.75',
    remote_pass='PW#bLj#@!0327',
    remote_user = 'root',
    extra_vars = {"ansible_ssh_port":"16333"}
)

try:
    x = api.command('top -bn 1 -i -c')

    #print(x)

    a = json.dumps(x)


    print(a)
except Exception as e:

    print(e)


