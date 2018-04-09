import os
import sys
from suitable import Api

import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO_DIR = os.path.join(BASE_DIR, 'dev_ops_test1')
sys.path.insert(0, os.path.abspath(DJANGO_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'dev_ops_test1.settings'
django.setup()

from server.models import ServerDetail


def scan_server_infos(server):
    """
    扫描硬件信息
    :return:
    """

    api = Api(
        server.ip,
        remote_pass=server.ssh_password,
        remote_user=server.ssh_name,
    )

    try:
        #api.command('top -bn 1 -i -c')
        x = api.command('top -bn 1 -i -c')

        # print(x)



        print(x)
    except Exception as e:

        print(e)


def exec_all_servers():
    servers = ServerDetail.objects.all()

    # 取出各种server 执行函数
    for server in servers:
        print(server.ip)


def main():
    scan_server_infos()


if __name__ == "__main__":
    main()
