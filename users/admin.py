from django.contrib import admin
from .models import Student, Staff, Admin, Editor,Profile


admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Admin)
admin.site.register(Editor)

