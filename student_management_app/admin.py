# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Staff, Courses, Subjects, Student, Attendance, AttendanceReport, LeaveReportStaff, LeaveReportStudent, FeedbackStaff, FeedbackStudent, NotificationStaff, NotificationStudent
# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel)