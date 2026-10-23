from django.contrib import admin
from .models import ChurchDetails
from .models import Announcements
from .models import Leader

# Register your models here.
admin.site.register(ChurchDetails)
admin.site.register(Announcements)
admin.site.register(Leader)