from django.urls import reverse
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages

from student_management_app.EmailBackEnd import EmailBackEnd
from .models import *
from django.core.files.storage import FileSystemStorage


# Create your views here.
def showDemoPage(request):
    return render(request, 'demo.html')

def loginPage(request):
    return render(request, 'login_page.html')

def doLogin(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method not supported</h2>')
    else:
        user= EmailBackEnd.authenticate(request, request.POST.get('email'), request.POST.get('password'))
        if user != None:
            login(request,user)
            if user.user_type=="1":
            #return redirect('get_user_details')
            #return HttpResponse('Email: '+request.POST.get('email')+'Password: '+request.POST.get("password"))
            #return HttpResponseRedirect('admin_home')
                return redirect('admin_home')
            elif user.user_type=="2":
                #return HttpResponseRedirect(reverse("staff_home"))
                return redirect('staff_home')
            else:
                return redirect('student_home')
        else:
            messages.error(request, 'Invalid Login')
            #return redirect('get_user_details')
            #return HttpResponse('Email: '+request.POST.get("email")+'Password: '+request.POST.get("password"))
            return HttpResponseRedirect('/')
    


#def GetUserDetails(request):
    #if request.user != None:
        #return HttpResponse('User: '+request.user.email+' usertype: '+str(request.user.user_type))
    #else:
        #return HttpResponse('Please login first')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


#def admin_home(request):
    #return render(request, 'hod_template/home_content.html')

def sign_ups(request):
    return render(request, "sign_ups.html")



def student_signup(request):
    courses=Courses.objects.all()
    session_years=SessionYearModel.objects.all()
    return render(request,"student_signup.html",{"courses":courses,"session_years":session_years})

def do_student_signup(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    address = request.POST.get("address")
    session_year_id = request.POST.get("session_year")
    course_id = request.POST.get("course")
    sex = request.POST.get("sex")

    profile_pic = request.FILES['profile_pic']
    fs = FileSystemStorage()
    filename = fs.save(profile_pic.name, profile_pic)
    profile_pic_url = fs.url(filename)

    #try:
    user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,first_name=first_name, user_type=3)
    user.student.address = address
    course_obj = Courses.objects.get(id=course_id)
    user.student.course_id = course_obj
    session_year = SessionYearModel.objects.get(id=session_year_id)
    user.student.session_year_id = session_year
    user.student.gender = sex
    user.student.profile_pic = profile_pic_url
    user.save()
    messages.success(request, "Successfully Added Student")
    return HttpResponseRedirect(reverse("show_login"))





def staff_signup(request):
    return render(request,"staff_signup.html")

def do_staff_signup(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    address=request.POST.get("address")

    try:
        user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=2)
        user.staff.address=address
        user.save()
        messages.success(request,"Successfully Created Staff")
        return HttpResponseRedirect(reverse("show_login"))
    except:
        messages.error(request,"Failed to Create Staff")
        return HttpResponseRedirect(reverse("show_login"))





def admin_signup(request):
    return render(request,"admin_signup.html")


def do_admin_signup(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")

    try:
        user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=1)
        user.save()
        messages.success(request,"Successfully Created Admin")
        return HttpResponseRedirect(reverse("show_login"))
    except:
        messages.error(request,"Failed to Create Admin")
        return HttpResponseRedirect(reverse("show_login"))