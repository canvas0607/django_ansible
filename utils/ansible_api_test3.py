import json
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
from ansible.inventory.host import Host, Group
from collections import defaultdict


class ResultCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin
    """

    def __init__(self):
        super(ResultCallback, self).__init__()
        self.res = defaultdict(dict)
        self.fail = []
        self.unre = []

    def v2_runner_on_ok(self, result, **kwargs):
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host_name = result._host
        msg = result._result.get('stdout',None)
        # print(json.dumps({host.name: result._result}, indent=4))
        # print(result._result['stdout_lines'])
        #res = result._result
        tmp_data = dict(msg=msg)
        self.res[host_name] = tmp_data

    def v2_runner_on_failed(self, result, ignore_errors=False):
        # res = result._result
        # self.fail.append(res)
        self.fail.append(result)

    def v2_runner_on_unreachable(self, result):
        # res = result._result
        # self.unre.append(res)
        self.unre.append(result)


class MyVariableManger(object):
    def __init__(self, *args, **kwargs):
        # 加载loader
        #self.loader = kwargs.get('loader', DataLoader())
        self.loader = DataLoader()

        # 加载invertory
        self.inventory = InventoryManager(loader=self.loader, sources=None)

        Options = namedtuple('Options',
                             ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check',
                              'diff'])

        self.options = Options(connection='local', module_path=None, forks=5, become=False, become_method=None,
                               become_user=None,
                               check=False,
                               diff=False)

        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)

        self.group = kwargs.get("group", 'default')

        self.passwords = dict(vault_pass='secret', become_pass='tusbasa1')

        self.run_hosts = []

    @property
    def variables(self):
        return self.variable_manager

    @variables.setter
    def variables(self, value):
        """
        设定要执行的host信息
        :param value:
        :return:
        """
        # TODO 遍历value 判断ip之类参数的正确性
        for i in value:
            hostname = i.get('hostname', None)
            port = i.get('host_port', '22')
            ip = i.get('host_ip', '127.0.0.1')
            password = i.get("password", None)
            user = i.get('user', None)
            tmp_host = Host(name=hostname)
            # tmp_host.add_group(self.group)
            self.run_hosts.append(hostname)
            self.variable_manager.set_host_variable(host=tmp_host, varname='ansible_ssh_host', value=ip)
            self.variable_manager.set_host_variable(host=tmp_host, varname='ansible_ssh_pass', value=password)
            self.variable_manager.set_host_variable(host=tmp_host, varname='ansible_ssh_port', value=port)
            self.variable_manager.set_host_variable(host=tmp_host, varname='ansible_ssh_user', value=user)
            self.inventory.add_host(host=hostname, port=port)

        if len(self.run_hosts) < 2:
            self.run_hosts = self.run_hosts[0]


class AnsibleApi(object):

    def __init__(self, variable_manager):
        self.variable_manager = variable_manager


    def run_ad_hoc(self,command):
        # # task = [
        # #     command
        # #     # dict(action=dict(module='raw', args='chkconfig --list | grep iptables'), register='shell_out'),
        # #     # dict(action=dict(module='ping'), register='shell_out'),
        # #     #dict(action=dict(module='shell', args='ifconfig')),
        # #     # dict(action=dict(module='apt',name='lua5.2',state='present'))
        # #     # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        # #     # dict(action=dict(module='ping')),
        # # ]
        # task = []
        # task.append(command)

        task = []
        task.append(command)
        play_source = dict(
            name="test1111",
            hosts=self.variable_manager.run_hosts,
            gather_facts='no',
            tasks=command
        )

        play = Play().load(play_source, variable_manager=self.variable_manager, loader=self.variable_manager.loader)

        tqm = None

        #self.results_callback = ResultCallback()

        results_callback = ResultCallback()
        try:
            tqm = TaskQueueManager(
                inventory=self.variable_manager.inventory,
                variable_manager=self.variable_manager.variable_manager,
                loader=self.variable_manager.loader,
                options=self.variable_manager.options,
                passwords=self.variable_manager.passwords,
                stdout_callback=results_callback,  # Use our custom callback instead of the ``default`` callback plugin
            )
            result = tqm.run(play)
            res = result
        finally:
            if tqm is not None:
                tqm.cleanup()


if __name__ == "__main__":
    var_man = MyVariableManger()
    var_man.variables = [
        dict(hostname=None, host_ip='111.231.203.175', host_port=None, password='pm13658034488', user='root'),
        dict(hostname='tst1', host_ip='111.231.203.174', host_port='22', password='pm13658034488', user='root'),
        dict(hostname='tst2', host_ip='127.0.0.1', host_port='22', password='tusbasa1', user='canvas')
    ]

    run_in = AnsibleApi(var_man)
    #command=dict(action=dict(module='shell', args='ifconfig')),
    task = [

        #dict(action=dict(module='raw', args='chkconfig --list | grep iptables'), register='shell_out'),
        dict(action=dict(module='ping'), register='shell_out'),
        #dict(action=dict(module='shell', args='ifconfig')),
        #{'action':{"module":"shell",'args':"ifconfig"}}
        #dict(action=dict(module='apt',name='lua5.2',state='present'))
        # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        #dict(action=dict(module='ping')),
    ]

    command = {'action':{"module":"shell",'args':"ifconfig"}}
    run_in.run_ad_hoc(task)
