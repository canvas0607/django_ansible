import os
import sys
import time
from suitable import Api

import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO_DIR = os.path.join(BASE_DIR, 'dev_ops_test1')
DJANGO_APP_DIR = os.path.join(BASE_DIR,'apps')
sys.path.insert(0, os.path.abspath(DJANGO_DIR))
sys.path.insert(0, os.path.abspath(BASE_DIR))
sys.path.insert(0, os.path.abspath(DJANGO_APP_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'dev_ops_test1.settings'
django.setup()

from server.models import ServerDetail, ServerStatus
from utils.re_fun import get_num


def scan_server_infos(server):
    """
    扫描硬件信息(cpu 内存 硬盘)
    :return:
    """
    api = Api(
        server.ip,
        remote_pass=server.ssh_password,
        remote_user=server.ssh_name,
        extra_vars={"ansible_ssh_port": server.ssh_port}
    )
    try:
        # 获取cpu 内存信息
        res = api.command('top -bn 1 -i -c')
        contacted_res = res['contacted']
        ip_res = contacted_res[server.ip]
        stdout_lines = ip_res['stdout_lines']
        # 获取cpu info
        cpu_info = stdout_lines[2]
        cpu_info_lines = cpu_info.split(',')
        cpu_left = cpu_info_lines[3]
        # 获取cpu使用率
        cpu_left_percent = str(100 - int(get_num(cpu_left.split('%')[0])))
        # 获取 memory info
        memory_info = stdout_lines[3]
        memory_info_lines = memory_info.split(',')
        # 获取内存使用/空余空间
        memory_info_used = get_num(memory_info_lines[1].lstrip().split(" ")[0])
        memory_info_free = get_num(memory_info_lines[2].lstrip().split(" ")[0])

        info = dict(status=True, server_ip=server.ip, cpu_per=cpu_left_percent, memory_use=memory_info_used,
                    memory_info_free=memory_info_free)
        return info
    except Exception as e:
        info = dict(status=False, server_ip=server.ip, msg=e)
        return info


def exec_all_servers():
    servers = ServerDetail.objects.all()

    # 取出各种server 执行函数
    for server in servers:
        res = scan_server_infos(server)
        if res['status']:
            ServerStatus.objects.update_or_create(
                server=server,
                defaults=dict(
                    memory_free=res['memory_info_free'],
                    memory_used=res['memory_use'],
                    cpu_per=res['cpu_per'],
                )
            )
        else:
            #如果连不通 则取消服务器状态
            server.server_is_active = False
            server.ssh_error_msg = False
            server.save()


def main():
    exec_all_servers()


if __name__ == "__main__":
    while True:
        main()
        time.sleep(10)
