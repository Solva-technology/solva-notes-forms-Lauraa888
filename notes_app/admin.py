from django.contrib import admin
from .models import User, Note, Category, Status 

admin.site.register(User)
admin.site.register(Note)
admin.site.register(Status)
admin.site.register(Category)