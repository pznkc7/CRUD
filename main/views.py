from django.shortcuts import render
from . models import StudentLeave
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'crudApp1/home.html')

def form(request):
    if request.method == "POST":
        roll_number = request.POST.get('rollnumber')
        full_name = request.POST.get('fullName')
        faculty = request.POST.get('faculty')
        semester = request.POST.get('semester')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        guardian_contact = request.POST.get('guardianContact')
        leave_type = request.POST.get('leaveType')
        student_email = request.POST.get('email')
        reason = request.POST.get('reason')

        StudentLeave.objects.create(
            roll_number=roll_number,
            full_name=full_name,
            faculty=faculty,
            semester=semester,
            start_date=start_date,
            end_date=end_date,  
            guardian_contact=guardian_contact,
            leave_type=leave_type,      
            student_email=student_email,
            reason=reason
        )

        subject = "Regarding your leave application"
        message = "hello"
        from_email = 'khatripujan35@gmail.com'#sender's email-id
        recipient_list = [student_email] #receiver's email-id
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)
    return render(request, 'crudApp1/form.html')

def about(request):
    return render(request, 'crudApp1/about.html')

def contact(request):
    return render(request, 'crudApp1/contact.html')