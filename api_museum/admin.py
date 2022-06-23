from django.contrib import admin
from api_museum.models import Artist
from api_museum.models import Meduim
from api_museum.models import Museum
from api_museum.models import CulturalProperty
# Register your models here.
admin.site.register(Artist)
admin.site.register(Meduim)
admin.site.register(Museum)
admin.site.register(CulturalProperty)