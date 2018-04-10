from suitable import Api
import json


api = Api(
    '183.61.128.75',
    remote_pass='PW#bLj#@!0327',
    remote_user = 'root',
    extra_vars = {"ansible_ssh_port":"16333"}
)


x = api.command('ifconfig').stdout()

print('adfa')

# try:
#     #获取cpu 内存信息命令
#     res = api.command('top -bn 1 -i -c')
#     contacted_res = res['contacted']
#     ip_res = contacted_res['183.61.128.75']
#     stdout_lines = ip_res['stdout_lines']
#     #获取cpu info
#     cpu_info = stdout_lines[2]
#     cpu_info_lines = cpu_info.split(',')
#     cpu_left = cpu_info_lines[3]
#     cpu_left_percent = cpu_left.split('%')[0]
#     #获取 memory info
#     memory_info = stdout_lines[3]
#     memory_info_lines = memory_info.split(',')
#     memory_info_used = memory_info_lines[1].lstrip().split(" ")[0]
#     memory_info_free = memory_info_lines[2].lstrip().split(" ")[0]
#
#     info = dict(cpu_per=cpu_left_percent,memory_use = memory_info_used,memory_info_free = memory_info_free)
#
#
#     #return info
# except Exception as e:
#
#     print(e)


