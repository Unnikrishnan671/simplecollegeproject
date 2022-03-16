from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from app1.models import student
from app1.models import course
# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')

@login_required(login_url='login')
def about(request):
    return render(request,'about.html')

@login_required(login_url='login')
def coursepage(request):
    return render(request,'course.html')

@login_required(login_url='login')
def studentpage(request):
    return render(request,'student.html')


def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exists!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                messages.info(request,'successfully completed...')
        else:
            messages.info(request,'Password doesnt match!!')
            return redirect('signup')
        return redirect('login')
    else:
        return render(request,'signup.html')

#user login functionality view
def login(request):
    try:
        if request.method == 'POST':
            try:
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(username=username,password=password)
                if user is not None:
                    auth.login(request,user)
                    messages.info(request, f'Welcome {username}')
                    return redirect('about')
                else:
                    messages.info(request, 'Invalid Username or password.Try again!')
                    return redirect('loginpage')
            except:
                messages.info(request,'Invalid username or password')
                return render(request,'login.html')
        else:
            # messages.info(request,'Oops,something went wrong')
            return render(request,'login.html')
    except:
        messages.info(request,'Invalid username or password')
        return render(request,'login.html')

@login_required(login_url='login')
def logout(request):
    # --login required method--
    auth.logout(request)
    return redirect('home')

@login_required(login_url='login')
def add_course(request):
    if request.method=='POST':
        cors=request.POST['course']
        cfee=request.POST['cfee']
        print(cors)
        crs=course()
        crs.course_name=cors
        crs.fee=cfee
        crs.save()
        print("hii")
        return redirect('student1')

@login_required(login_url='login')
def add_student(request):
    if request.method=='POST':
        sname=request.POST['sname']
        address=request.POST['address']
        age=request.POST['age']
        jdate=request.POST['jdate']
        sel1 = request.POST['sel']
        course1=course.objects.get(id=sel1)
        std=student(std_name=sname,
                    std_address=address,
                    std_age=age,
                    join_date=jdate,
                    course=course1)
        std.save()
        print("hii")
        return redirect('show')

@login_required(login_url='login')
def course1(request):
    uid = User.objects.get(id=request.session["uid"])
    return render(request, 'course.html',{'uid':uid})

@login_required(login_url='login')
def student1(request):
    courses=course.objects.all()
    context={'courses':courses}
    return render(request,'student.html',context)

@login_required(login_url='login')
def show(request):
    studs=student.objects.all()
    return render(request,'show.html',{'studs':studs})
