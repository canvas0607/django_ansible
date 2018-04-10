from .models import ServerDetail, ServerStatus
import xadmin


class ServerDetailAdmin(object):
    class ServerStatusInline(object):
        model = ServerStatus

    inlines = [ServerStatusInline]


xadmin.site.register(ServerDetail, ServerDetailAdmin)
