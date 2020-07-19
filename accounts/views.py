from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from education.models import User_Register
from django.contrib import messages

def home_register(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email_id = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request,"Username taken...")
            return redirect('home_register')
        elif User.objects.filter(email=email_id).exists():
            messages.info(request,"Email already registered...")
            return redirect('home_register',)
        else:
            if password1==password2:
                user = User.objects.create_user(username=username, password=password1, email=email_id, first_name=first_name, last_name=last_name)
                user.save()
                print('User created...')
                user = auth.authenticate(username=username, password=password1)
                if user is not None:
                    auth.login(request, user)
                return redirect('/')
                #return redirect('register',register)
                                #,{'first_name': first_name, 'last_name':last_name, 'email':email_id})
            else:
                messages.info(request,"Password not matching...")
                return redirect('home_register')
    else:
        return render(request, 'home_register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials...')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

#def register_home(request):
#    return render(request, 'register_home.html')

def register(request):
    if request.method == 'POST':
        disp_type = request.POST.get("regtype", None)
        if disp_type in ["Teacher"]:
            reg_type = "Teacher"
        elif disp_type in ["Student"]:
            reg_type = "Student"
        else:
            reg_type = "Guardian"
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        address = request.POST['address']
        disp_gender = request.POST.get("gender", None)
        if disp_gender in ["Male"]:
            gender = "Male"
        elif disp_gender in ["Female"]:
            gender = "Female"
        else:
            gender = "Other"
#        username = request.POST['username']
        email_id = request.POST['email']
        guardian_name = request.POST['guardian_name']
        state = request.POST['state']
        city = request.POST['city']
        pincode = request.POST['pincode']
        dob = request.POST['birth_date']
        course = request.POST['course']
        primary_num = request.POST['phone1']
        secondary_num = request.POST['phone2']

        obj1 = User_Register(reg_type=reg_type, first_name=first_name, last_name=last_name, 
                                                          address=address, gender=gender, email_id=email_id,
                                                          guardian_name=guardian_name,state=state,city=city, pincode=pincode,
                                                          dob=dob, course=course, primary_num=primary_num, secondary_num=secondary_num)
        obj1.save()

        return redirect('/')
#    elif request.method == 'POST':
#        pass
    else:
        return render(request,'register.html')