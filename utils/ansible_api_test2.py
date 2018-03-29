import json
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
from ansible.inventory.host import Host, Group
from ansible.executor.playbook_executor import PlaybookExecutor


class ResultCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin
    """

    def __init__(self):
        super(ResultCallback, self).__init__()
        self.res = []
        self.fail = []
        self.unre = []

    def v2_runner_on_ok(self, result, **kwargs):
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host = result._host
        # print(json.dumps({host.name: result._result}, indent=4))
        # print(result._result['stdout_lines'])
        res = result._result
        self.res.append(res)

    def v2_runner_on_failed(self, result, ignore_errors=False):
        res = result._result
        self.fail.append(res)

    def v2_runner_on_unreachable(self, result):
        res = result._result
        self.unre.append(res)


Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
# initialize needed objects
loader = DataLoader()
options = Options(connection='local', module_path=None, forks=5, become=True, become_method='sudo', become_user='root',
                  check=False,
                  diff=False)

# options = Options(connection='local', module_path=None, forks=5, become=None, become_method=None, become_user=None, check=False,
#                  diff=False)
passwords = dict(vault_pass='secret', become_pass='tusbasa1')

# Instantiate our ResultCallback for handling results as they come in
results_callback = ResultCallback()

# create inventory and pass to var manager
inventory = InventoryManager(loader=loader, sources=None)

# variable_manager = VariableManager(loader=loader, inventory=inventory)
hostname = 'test1'
hostport = 22
hostip = '127.0.0.1'
password = 'tusbasa1'
username = 'canvas'
variable_manager = VariableManager(loader=loader, inventory=inventory)

my_host = Host(name=hostname, port=hostport)

variable_manager.set_host_variable(host=my_host, varname='ansible_ssh_host', value=hostip)
variable_manager.set_host_variable(host=my_host, varname='ansible_ssh_pass', value=password)
variable_manager.set_host_variable(host=my_host, varname='ansible_ssh_port', value=hostport)
variable_manager.set_host_variable(host=my_host, varname='ansible_ssh_user', value=username)
# variable_manager.set_host_variable(host=my_host,varname='ansible_become_pass',value='tusbasa1')
# variable_manager.set_host_variable(host=my_host,varname='ansible_become',value=True)
# variable_manager.set_host_variable(host=my_host,varname='ansible_become_method',value='sudo')
# variable_manager.set_host_variable(host=my_host,varname='ansible_become_user',value='root')


task = [
    # dict(action=dict(module='raw', args='chkconfig --list | grep iptables'), register='shell_out'),
    # dict(action=dict(module='ping'), register='shell_out'),
    dict(action=dict(module='shell', args='ifconfig')),
    # dict(action=dict(module='apt',name='lua5.2',state='present'))
    # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
    # dict(action=dict(module='ping')),
]

# create play with tasks
play_source = dict(
    name="test1111",
    hosts='127.0.0.1',
    gather_facts='no',
    tasks=task
)
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# actually run it
tqm = None
try:
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords,
        stdout_callback=results_callback,  # Use our custom callback instead of the ``default`` callback plugin
    )
    result = tqm.run(play)
    res = result
finally:
    if tqm is not None:
        tqm.cleanup()
