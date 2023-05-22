from django.shortcuts import render, redirect
from . models import *
from random import randint
from django.shortcuts import get_object_or_404
# Create your views here.

def IndexPage(request):
    return render(request, "app/index.html")

def About(request):
    return render(request, "app/about.html")

def Contact(request):
    return render(request,"app/contact.html")


def SignupPage(request):
    return render(request,"app/signup.html")


def RegisterUser(request):
    if request.POST['role'] == "Candidate":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname =  request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User Already Exist!"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcan = Candidate.objects.create(user_id= newuser, firstname=fname,lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})

    else:
        print("Company Registration")
        if request.POST['role'] == "Company":
            role = request.POST['role']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']

            comp = UserMaster.objects.filter(email=email)

        if comp:
            message = "Company Already Exist!"
            return render(request, "app/signup.html", {'msg': message})
        else:
            if password == cpassword:
                otp = randint(100000, 999999)
                newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)
                newcomp = Company.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                return render(request, "app/otpverify.html", {'email': email})

    # else:
    #     print("Company Registration")
    #     if request.POST['role'] == "Company":
    #         role = request.POST['role']
    #         fname = request.POST['firstname']
    #         lname =  request.POST['lastname']
    #         email = request.POST['email']
    #         password = request.POST['password']
    #         cpassword = request.POST['cpassword']

    #         comp = UserMaster.objects.filter(email=email)

    #     if comp:
    #         message = "Company Already Exist!"
    #         return render(request,"app/signup.html",{'msg':message})
    #     else:
    #         if password == cpassword:
    #             otp = randint(100000,999999)
    #             newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
    #             newcan = Company.objects.create(user_id= newuser, firstname=fname,lastname=lname)
    #             return render(request,"app/otpverify.html",{'email':email})


def OTPPage(request):
    return render(request,"app/otpverify.html")


def Otpverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)

    if user:
        if user.otp == otp:
            message = "OTP Verify Successfully"
            return render(request,"app/login.html", {'msg':message})
        
        else:
            message = "OTP is incorrect"
            return render(request,"app/otpverify.html", {'msg':message})
        
    else:
        return render(request,"app/signup.html")
    

def Loginpage(request):
    return render(request,"app/login.html")


def LoginUser(request):
    if request.POST['role'] == "Candidate":
        email = request.POST['email']
        password = request.POST['password']

        user = UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=="Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                return redirect('index')
            else:
                message = "Password Does not Match!"
                return render(request,"app/login.html",{'msg': message})
            
        else:
            message = "User Does not exist!"
            return render(request,"app/login.html",{'msg': message})
    
    else:
        if request.POST['role'] == "Company":
            email = request.POST['email']
            password = request.POST['password']

            user = UserMaster.objects.get(email=email)
            if user:
                if user.password==password and user.role=="Company":
                   can = Company.objects.get(user_id=user)
                   request.session['id'] = user.id
                   request.session['role'] = user.role
                   request.session['firstname'] = can.firstname
                   request.session['lastname'] = can.lastname
                   request.session['email'] = user.email
                   return redirect('index')
            else:
                message = "Password Does not Match!"
                return render(request,"app/login.html",{'msg': message})
            
        else:
            message = "User Does not exist!"
            return render(request,"app/login.html",{'msg': message})
        

# def ProfilePage(request,pk):
#     user = UserMaster.objects.get(pk=pk)
#     can = Candidate.objects.get(user_id = user)
#     return render(request, "app/profile.html",{'user':user,'can':can})

def ProfilePage(request, pk):
    user = get_object_or_404(UserMaster, pk=pk)
    try:
        can = Candidate.objects.get(user_id=user)
    except Candidate.DoesNotExist:
        can = None
    return render(request, "app/profile.html", {'user': user, 'can': can})

def UpdateProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        can.firstname = request.POST['firstname']
        can.lastname = request.POST['lastname']
        can.state = request.POST['state']
        can.city = request.POST['city']
        can.job_type = request.POST['jobtype']
        can.jobcategory = request.POST['jobcategory']
        can.education = request.POST['education']
        can.experiance = request.POST['experience']
        can.min_salary = request.POST['minsalary']
        can.max_salary = request.POST['maxsalary']
        can.contact = request.POST['contact']
        can.gender = request.POST['gender']
        can.jondescription = request.POST['description']
        can.country = request.POST['country']
        can.profile_pic = request.FILES.get('myfile')
        can.save()
        print("Data Saved")
        url = f'/profile/{pk}'
        return redirect(url)
    
    # else:
    #     if user.role == "Company":
    #        can = Company.objects.get(user_id=user)
    #        can.firstname = request.POST['firstname']
    #        can.lastname = request.POST['lastname']
    #        can.state = request.POST['state']
    #        can.city = request.POST['city']
    #     #    can.job_type = request.POST['jobtype']
    #     #    can.jobcategory = request.POST['jobcategory']
    #     #    can.education = request.POST['education']
    #     #    can.experiance = request.POST['experience']
    #     #    can.min_salary = request.POST['minsalary']
    #     #    can.max_salary = request.POST['maxsalary']
    #        can.contact = request.POST['contact']
    #     #    can.gender = request.POST['gender']
    #     #    can.jondescription = request.POST['description']
    #     #    can.country = request.POST['country']
    #     #    can.profile_pic = request.FILES.get('myfile')
    #        can.save()
    #        print("Data Saved")
    #        url = f'/profile/{pk}'
    #        return redirect(url)


