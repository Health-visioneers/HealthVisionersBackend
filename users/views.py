from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView , LogoutView
from .forms import SignUpForm, LoginForm
from django.contrib.auth import views as auth_views

def UserSignup(request, user_type):
    if request.user.is_authenticated:
        return redirect('home')

    if user_type == 'patient':
        form_class = SignUpForm
    elif user_type == 'doctor':
        form_class = SignUpForm
    elif user_type == 'hospital_staff':
        form_class = SignUpForm
    else:
        return redirect('login')

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            user = form.save()
            if user_type == 'patient':
                user.is_patient = True
                user.save()
            elif user_type == 'doctor':
                user.is_doctor = True
                user.save()
            elif user_type == 'hospital_staff':
                user.is_hospital_staff = True
                user.save()
            login(request, user)
            return redirect('home')
    else:
        form = form_class()

    return render(request, 'signup_form.html', {'form': form , 'user_type': user_type})



class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        remember_me = self.request.POST.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
        return super().form_valid(form)
    



class UserLogoutView(auth_views.LogoutView):
    next_page = 'login'  # Redirect to home page after logout
    
    
    
    
from .forms import PatientForm, DoctorForm, HospitalStaffForm
from .models import Patient, Doctor, HospitalStaff

def userhome(request):
    if request.user.is_authenticated:
        context = {}
        form = None
        if request.user.is_patient:
            context['user_type'] = 'patient'
            if not Patient.objects.filter(user=request.user).exists():
                form = PatientForm(request.POST or None)
            else:
                return render(request, 'home.html')
        elif request.user.is_doctor:
            context['user_type'] = 'doctor'
            if not Doctor.objects.filter(user=request.user).exists():
                form = DoctorForm(request.POST or None)
            else:
                return render(request, 'home.html')
        elif request.user.is_hospital_staff:
            context['user_type'] = 'hospital_staff'
            if not HospitalStaff.objects.filter(user=request.user).exists():
                form = HospitalStaffForm(request.POST or None)
            else:
                return render(request, 'home.html')

        if form and form.is_valid():
            if request.user.is_patient:
                patient = Patient.objects.create(user=request.user, **form.cleaned_data)
                return redirect('home')
            elif request.user.is_doctor:
                doctor = Doctor.objects.create(user=request.user, **form.cleaned_data)
                return redirect('home')
            elif request.user.is_hospital_staff:
                hospital_staff = HospitalStaff.objects.create(user=request.user, **form.cleaned_data)
                return redirect('home')

        context['form'] = form
        return render(request, 'details.html', context)
    else:
        return redirect('login')