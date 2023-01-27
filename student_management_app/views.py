from django.urls import reverse
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages

from student_management_app.EmailBackEnd import EmailBackEnd


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

