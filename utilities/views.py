# myapp/views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from .models import UserProfile
from .forms import CustomUserCreationForm
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse

@staff_member_required
def support_dashboard(request):
    # Retrieve service requests
    service_requests = ServiceRequest.objects.all()
    return render(request, 'support_dashboard.html', {'service_requests': service_requests})

def view_service_request(request, request_id):
    # Retrieve individual service request
    service_request = ServiceRequest.objects.get(id=request_id)
    return render(request, 'view_service_requests.html', {'service_request': service_request})



# def update_service_request_status(request, request_id):
#     # Update status of a service request
#     if request.method == 'POST':
#         service_request = ServiceRequest.objects.get(id=request_id)
#         new_status = request.POST.get('status')
#         service_request.status = new_status
#         service_request.save()
#         return redirect('support_dashboard')
#     # Handle GET request (display form)
#     service_request = ServiceRequest.objects.get(id=request_id)
#     return render(request, 'update_service_request_status.html', {'service_request': service_request})




@login_required
def view_service_requests(request):
    # Fetch service requests for the current user
    service_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'view_service_request.html', {'service_requests': service_requests})



@staff_member_required
def update_service_request_status(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        service_request.status = status
        service_request.save()
        return redirect('support_dashboard')  # Redirect to the support dashboard
    return render(request, 'update_service_request_status.html', {'service_request': service_request})



def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('profile')  # Redirect to user profile after submission
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a UserProfile object for the new user
            UserProfile.objects.create(
                user=user,
                bio=form.cleaned_data.get('bio'),
                email=form.cleaned_data.get('email'),
                phone_number=form.cleaned_data.get('phone_number'),
                address=form.cleaned_data.get('address')
            )
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def profile(request):
    user_profile = request.user.userprofile
    return render(request, 'profile.html', {'user_profile': user_profile})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the user's profile page
            return redirect('profile')
        else:
            # Handle invalid login credentials
            return render(request, 'registration/login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'registration/login.html')

def index(request):
    return render(request,'index.html')
