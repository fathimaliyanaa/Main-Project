from django.contrib import admin

# Register your models here.
# 1. user_login , staff_details , dataset_master , query_history 
# 5. feedback 
from .models import user_login, user_details

from.models import staff_details , dataset_master , query_history 
from.models import feedback


admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(staff_details)
admin.site.register(dataset_master)
admin.site.register(query_history)
admin.site.register(feedback)