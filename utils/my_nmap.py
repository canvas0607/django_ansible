import nmap


# nm = nmap.PortScanner()
# res = nm.scan(hosts='119.146.207.92',arguments='-F -sT -v')

#print(res)


class MyNamp(object):

    def __init__(self,ip,ports=None):
        self.nm = nmap.PortScanner()
        if not isinstance(ip,list):
            ip = [ip]
        self.ip = ip
        self.ports = ports


    #
    def fast_scan(self):

        res = []

        for i in self.ip:

            res.append(self.nm.scan(hosts=i,arguments='-F -sT -v'))

        return res

ip_list = ['119.146.207.92','119.146.207.80']
scaner = MyNamp(ip_list)

res = scaner.fast_scan()

print(res)









