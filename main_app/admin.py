from django.contrib import admin
from .models import Collection, Store, Stamp

# Register your models here.
admin.site.register(Stamp)
admin.site.register(Collection)
admin.site.register(Store)