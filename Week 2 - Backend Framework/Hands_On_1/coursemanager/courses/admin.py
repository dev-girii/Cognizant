from django.contrib import admin
from .models import Department, Course, Student, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # 23. Show multiple columns in the list view
    list_display = ['name', 'code', 'credits', 'department']
    
    # 23. Enable search box for course name and code
    search_fields = ['name', 'code']
    
    # 24. Enable right-hand sidebar filtering by department
    list_filter = ['department']

# Register remaining models so they are visible in the admin dashboard
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Enrollment)