from .models import ServerDetail,ServerStatus
import xadmin
class ServerDetailAdmin(object):
    pass

xadmin.site.register(ServerDetail,ServerDetailAdmin)


