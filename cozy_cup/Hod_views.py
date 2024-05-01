from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from app.models import Course,Session,Student,CustomUser,Staff,Subject
from django.contrib import messages

from cozy_cup import Staff_views

@login_required(login_url='/login/')
def Home(request):
    student_count=Student.objects.all().count()
    course_count=Course.objects.all().count()
    subject_count=Subject.objects.all().count()
    staff_count=Staff.objects.all().count()
    
    student_gender_male=Student.objects.filter(gender='Male').count()
    student_gender_female=Student.objects.filter(gender='Female').count()

    context={
        'staff_count':staff_count,
        'student_count':student_count,
        'course_count':course_count,
        'subject_count':subject_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female

    }
    
    return render(request,'Hod/home.html',context)

@login_required(login_url='/')
def Add_student(request):
    
    course = Course.objects.all()
    
    session_year = Session.objects.all()

  

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
           messages.warning(request,'Email Is Already Taken')
           return redirect('Add_student')
        if CustomUser.objects.filter(username=username).exists():
           messages.warning(request,'Username Is Already Taken')
           return redirect('Add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session.objects.get(id=session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('View_student')



    context = {
        'course':course,
        'session_year':session_year,
    }

    return render(request,'Hod/add_student.html',context)
def View_student(request):
    student=Student.objects.all()
    context={
         'student':student,
    }

    
    return render(request,'Hod/views_student.html',context)
def Edit_student(request,id):
    student=Student.objects.filter(id = id)
    course=Course.objects.all()
    session_year=Session.objects.all()
    context={
        'student':student,
        'course':course,
        'session_year':session_year,
    }
    return render(request,'Hod/edit_student.html',context)


  

def Update_student(request):
    if(request.method=="POST"):
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        user=CustomUser.objects.get(id=student_id)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username
        if password!=None and password!="":
                user.set_password(password)
        if profile_pic!=None and profile_pic!="":
                user.profile_pic=profile_pic
        user.save()
        student=Student.objects.get(admin=student_id)
        student.address=address
        student.gender=gender
        course=Course.objects.get(id=course_id)
        student.course_id=course
        session_year=Session.objects.get(id=session_year_id)
        student.session_year_id=session_year
        student.save()
        messages.success(request,"record are sucessfully updated")
        return redirect('View_student')


    return render(request,'Hod/Update_student.html')
def Delete_student(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record Are Successfully Deleted !')
    return redirect('View_student')
def Add_course(request):
    if request.method=="POST":
        course_name = request.POST['course_name']
        
        course=Course(
            name=course_name
        )
        course.save()
        messages.success(request,"course are sucessfully created")
        return redirect('Add_course')

    return render(request, 'Hod/add_course.html')
def View_course(request):
    course = Course.objects.all()
    context={
        'course':course,
    }
    return render(request, 'Hod/view_course.html',context)

def Edit_course(request,id):
    course = Course.objects.get(Course, id=id)
    context = {
        'course': course,  # Convert the single course to a list
    }
    return render(request, 'Hod/edit_course.html',context)
def Update_course(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')
        
        # Use 'objects' instead of 'object'
        course = Course.objects.get(id=course_id)
        
        course.name = name 
        course.save()

        # Redirect to the Edit_course view for the updated course
        return redirect('Edit_course', id=course.id)

def Add_staff(request):
    if(request.method=="POST"):
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        if CustomUser.objects.filter(email=email).exists():
           messages.warning(request,'Email Is Already Taken')
           return redirect('Add_staff')
        if CustomUser.objects.filter(username=username).exists():
           messages.warning(request,'Username Is Already Taken')
           return redirect('Add_staff')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2,
               
            )
            user.set_password(password) 
            user.save()
            staff=Staff(
                admin=user,
                address=address,
                gender=gender
            )
            staff.save()
            messages.warning(request,"staff are sucessfully added")
            return redirect('Add_staff')
    return render(request, 'Hod/add_staff.html')
def View_staff(request):
    staff=Staff.objects.all()
    context={
     'staff':staff
}
    return render(request, 'Hod/view_staff.html',context)
def Edit_staff(request,id):
    
    staff=Staff.objects.get(id=id)
    context={
        'staff':staff
    }
    return render(request, 'Hod/edit_staff.html',context)
def Update_staff(request):
    if(request.method=="POST"):
        
        staff_id = request.POST.get('staff_id')

        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        user=CustomUser.objects.get(id=staff_id)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username
        if password!=None and password!="":
                user.set_password(password)
        if profile_pic!=None and profile_pic!="":
                user.profile_pic=profile_pic
        user.save()
        staff=Staff.objects.get(admin=staff_id)
        staff.gender=gender
        staff.address=address
        staff.save()
        messages.success(request,"staff data inserted sucessfully")
        return redirect('View_staff')
        
    return render(request, 'Hod/edit_staff.html')
def Delete_staff(request,admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request,'Record Are Successfully Deleted !')
    return redirect('View_staff')

def Add_subject(request):
    course=Course.objects.all()
    staff=Staff.objects.all()
    if(request.method=="POST"):
        subject_name=request.POST.get('subject_name')
        course_id=request.POST.get('course_id')
        staff_id=request.POST.get('staff_id')

        course=Course.objects.get(id=course_id)
        staff=Staff.objects.get(id=staff_id)
        
        subject=Subject(
            name=subject_name,
            course=course,
            staff=staff
        )
        subject.save()
        messages.success(request,"subject are sucessfully added")
        return redirect('Add_subject')

    context = {
    'course': course,
    'staff': staff
}

    return render(request, 'Hod/add_subject.html',context)	
def View_subject(request):
    subject=Subject.objects.all()
    context={
        'subject':subject
    }
    return render(request, 'Hod/view_subject.html',context)
def Edit_subject(request,id):
    
    subject=Subject.objects.get(id=id)
    course=Course.objects.all()
    staff=Staff.objects.all()
    context={
        'subject':subject,
        'course':course,
        'staff':staff,
    }
    return render(request, 'Hod/edit_subject.html',context)
def Update_subject(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        subject_name = request.POST.get('subject_name')

        # Retrieve the Course and Staff objects based on their IDs
        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        # Retrieve the Subject object to update
        subject = Subject.objects.get(id=subject_id)

        # Update the fields of the Subject object
        subject.name = subject_name
        subject.course = course
        subject.staff = staff

        # Save the updated Subject object
        subject.save()

        messages.success(request, "Subject updated successfully")
        return redirect('View_subject')

    return render(request, 'Hod/update_subject.html')
def Delete_subject(request,id):
    subject = Subject.objects.filter(id = id)
    subject.delete()
    messages.success(request,'Subject Are Successfully Deleted !')
    return redirect('View_subject')


def Add_session(request):
    if(request.method == "POST"):
        session_year_start=request.POST.get('session_year_start')
        session_year_end=request.POST.get('session_year_end')
        session=Session(
            session_start=session_year_start,
            session_end=session_year_end
        )
        session.save()
        messages.success(request,"session are sucessfully Added")
        return redirect('Add_session')

    return render(request, 'Hod/add_session.html')
def View_session(request):
    session = Session.objects.all()
    context = {
        'session': session
    }
    return render(request, 'Hod/view_session.html', context)
def Edit_session(request, id):
    session = Session.objects.filter(id=id)
    context={
        'session':session
    }
    return render(request,'Hod/edit_session.html',context)
def Staff_send_notification(request):
    staff=Staff.objects.all()
    context={
        'staff':staff
    }
    return render(request,'Hod/staff_notification.html',context)
def Staff_apply_leave(request):

    return render(request,'Hod/staff_leave.html')


