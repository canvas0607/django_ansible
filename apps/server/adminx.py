from .models import ServerDetail
import xadmin
class ServerDetailAdmin(object):
    pass

xadmin.site.register(ServerDetail,ServerDetailAdmin)


