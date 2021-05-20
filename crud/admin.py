from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Member)
admin.site.register(Famille)
admin.site.register(Mere)
admin.site.register(Enfant)
admin.site.register(Pere)
admin.site.register(Document)
admin.site.register(Ajax)
admin.site.register(CsvUpload)