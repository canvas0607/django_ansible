import nmap

# class Nmap(object):
#     def __init__(self,ip):
#         self.ip = ip
#         self.nm = nmap.PortScanner()
#         self.arguments = '-n -sP -PE'
#
#     def conn(self):
#         return self.nm.scan(self.ip, arguments=self.get_arguments())
#
#
#     def set_arguments(self,arguments):
#         self.arguments = arguments
#
#     def get_arguments(self):
#         return self.arguments
#
#     def is_active(self):
#         data = self.conn()
#         # 探测服务器是否存活
#         status = data['nmap']['scanstats']['uphosts']
#
#         if int(status) == 1:
#             return True
#
#         return False


class TestNmap(object):


    def __init__(self,ip):
        self.ip = ip
        self.nm = nmap.PortScanner()
        self.arguments = '-n -sP -PE'

    @classmethod
    def conn(cls,ip):
        obj = cls(ip=ip)
        res = obj.nm.scan(ip,arguments=obj.get_arguments)
        return res

    def set_arguments(self, arguments):
        self.arguments = arguments

    def get_arguments(self):
        return self.arguments

