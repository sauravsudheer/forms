
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import *
from .forms import RegistrationForm
from .forms import RegistrationNumberForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_profile= form.save()
            return redirect('success', registration_number=user_profile.registration_number)
    else:
        form = RegistrationForm()
    centers = Center.objects.all()
    return render(request, 'register.html',{'centers':centers, 'form':form})
def success(request, registration_number):
    return render(request, 'success.html', {'registration_number': registration_number})
def userdisplay(request):
    user_profile = None
    error_message = None

    if request.method == 'POST':
        form = RegistrationNumberForm(request.POST)
        if form.is_valid():
            registration_number = form.cleaned_data['registration_number']
            try:
                user_profile = UserProfile.objects.get(registration_number=registration_number)
            except UserProfile.DoesNotExist:
                error_message = 'User with the provided registration number does not exist.'
    else:
        form = RegistrationNumberForm()
    centers = Center.objects.all()
    return render(request, 'userdisplay.html', {'form': form, 'user_profile': user_profile, 'error_message': error_message, 'centers': centers})
def generate_pdf(request, registration_number):
    user_profile = get_object_or_404(UserProfile, registration_number=registration_number)
    
    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter)

    # Draw things on the PDF. Here's where the PDF generation happens.
    p.drawString(100, 750, f"User Details for Registration Number: {user_profile.registration_number}")
    p.drawString(100, 730, f"Name: {user_profile.name}")
    p.drawString(100, 710, f"Father's Name: {user_profile.fathername}")
    p.drawString(100, 690, f"Mother's Name: {user_profile.mothername}")
    p.drawString(100, 670, f"Email: {user_profile.email}")
    p.drawString(100, 650, f"Phone: {user_profile.phone}")
    p.drawString(100, 630, f"Center: {user_profile.center.centername}")
    p.drawString(100, 610, f"Medium: {user_profile.get_medium_display()}")

    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="user_details_{registration_number}.pdf"'
    return response
# Create your views here.
