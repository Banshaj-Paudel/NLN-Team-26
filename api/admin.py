from django.contrib import admin
from .models import Anchor, BurnMapResult, CheckIn, Session

admin.site.register(Anchor)
admin.site.register(CheckIn)
admin.site.register(BurnMapResult)
admin.site.register(Session)
