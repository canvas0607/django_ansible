import paramiko

class Paramiko(object):

    def __init__(self,host='127.0.0.1',port=22,password=None,username="",rsa_file=None):
        self.port= port
        self.host = host
        self.username = username
        self.pwd = password
        self.rsa_file = rsa_file
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def conn(self):
        if not self.rsa_file:
            try:
                self.ssh.connect(hostname=self.host, port=self.port, username=self.username, password=self.pwd)
            except Exception:
                return None


    def command(self):
        self.conn()
        stdin, stdout, stderr = self.ssh.exec_command('ls')
        return stdout




def test():
    ssh = Paramiko(host='127.0.0.1',port=22,username='canvas',password='tusbasa1')
    print(ssh.command())


if __name__ == '__main__':
    test()

