import os
import sys
from telnetlib import Telnet
from utils.my_nmap import Nmap


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.join(BASE_DIR, 'apps'))

os.environ["DJANGO_SETTINGS_MODULE"] = 'dev_ops_test1.settings'
import django
from django.utils import timezone
django.setup()

from server.models import ServerDetail

def main():
    #获取当前时间
    time_now = timezone.now()
    #获取在后台录入的服务器
    servers = ServerDetail.objects.all()
    if not servers:
        print('no servers')
        return



    #遍历所有服务器 获取信息
    #TODO 异步读取
    for server in servers:
        #把ip存入列表用于nmap扫描
        ip = server.ip
        ssh_port = server.ssh_port
        #通过nmap判断是否存活
        status = Nmap(ip).is_active()
        server.server_is_active = status
        #如果存活就Telnet ssh端口 进行ssh登录
        if status:
            #判断ssh 端口是否有效
            try:
                tn = Telnet(ip, port=ssh_port, timeout=10)
                res = tn.read_until(b'\n',timeout=10)
                if res:
                    server.ssh_is_active = True
                    server.ssh_error_msg = ""
                else:
                    server.ssh_is_active = False

                tn.close()
            except Exception as e:
                server.ssh_is_active = False
                server.ssh_error_msg = e

        #通过paramiko来登录服务器获取服务器信息



        server.last_scan_time = time_now
        server.save()


    print(nmap_datas)

if __name__ == '__main__':
    main()