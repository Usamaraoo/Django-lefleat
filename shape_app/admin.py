from django.contrib import admin
from .models import Pointing, Pakistan, Areas
from leaflet.admin import LeafletGeoAdmin


class PointAdmin(LeafletGeoAdmin):
    pass


class PakAdmin(LeafletGeoAdmin):
    pass


class AreaAdmin(LeafletGeoAdmin):
    pass


admin.site.register(Pointing, PointAdmin)
admin.site.register(Pakistan, PakAdmin)
admin.site.register(Areas, AreaAdmin)
