#

### 1.ANSIBLE API 说明

#### a.ansible api 基础逻辑

##### ansible api 官方简单调用

```python


#!/usr/bin/env python
import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C


class ResultCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin
    """

    def v2_runner_on_ok(self, result, **kwargs):
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))


Options = namedtuple('Options',
                     ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
# initialize needed objects
loader = DataLoader()
options = Options(connection='local', module_path=None, forks=100, become=None, become_method=None,
                  become_user=None, check=False,
                  diff=False)
passwords = dict(vault_pass='secret')

# Instantiate our ResultCallback for handling results as they come in
results_callback = ResultCallback()

# create inventory and pass to var manager
# use path to host config file as source or hosts in a comma separated string
inventory = InventoryManager(loader=loader, sources='localhost,')
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create play with tasks
play_source = dict(
    name="Ansible Play",
    hosts='localhost',
    gather_facts='no',
    tasks=[
        dict(action=dict(module='shell', args='ls'), register='shell_out'),
        dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
    ]
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
finally:
    if tqm is not None:
        tqm.cleanup()

        # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)


```

##### 代码逻辑梳理

1.首先理解 ansible 在命令行中执行逻辑

```python

$ ansible -i inventory all -m ping
```

-i 指定清单文件

all 要操作的任务组

-m 要执行的命令模块

> 备注:上面命令行能执行成功需要在执行路径下面或者ansible指定清单文件位置中配置hosts文件,表示可以执行那些服务器,或者组
>比如以下文件 /etc/ansible/hosts

```python

mail.example.com

[webservers]
foo.example.com
bar.example.com

[dbservers]
one.example.com
two.example.com
three.example.com

```

2.api中如何实现的

清单管理
```python

# create inventory and pass to var manager
# use path to host config file as source or hosts in a comma separated string
inventory = InventoryManager(loader=loader, sources='localhost,')
variable_manager = VariableManager(loader=loader, inventory=inventory)


```

a.InventoryManager 相当于上面-i命令后面需要使用的hosts 信息, 所以会在初始化的时候传递 loader进来,
目的是解析传递进来的hosts信息

b.VariableManager 完善inventory信息,比如用户名 密码 ssh端口号

执行任务参数
```python

# create play with tasks
play_source = dict(
    name="Ansible Play",
    hosts='localhost',
    gather_facts='no',
    tasks=[
        dict(action=dict(module='shell', args='ls'), register='shell_out'),
        dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
    ]
)

```

a.play_source就如同上面的命令行命令, 给执行的任务定义一个名称,要对hosts中的哪些host执行任务,
是否打印执行命令的明细(关闭加快执行速度),


