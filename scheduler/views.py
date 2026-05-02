from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils.algorithm import timetable_to_dict, generate_timetable
from .utils.csv_loader import load_data_from_csv
import os


def landing(request):
    """Front page — shown to everyone (logo + Login / Sign Up buttons)."""
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'scheduler/landing.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        tab = request.POST.get('tab', 'login')

        if tab == 'signup':
            # ── Sign-up ──────────────────────────────────────
            full_name  = request.POST.get('full_name', '').strip()
            email      = request.POST.get('email', '').strip()
            password   = request.POST.get('password', '')
            password2  = request.POST.get('password2', '')

            if not full_name or not email or not password:
                messages.error(request, 'Please fill in all fields.')
                return render(request, 'scheduler/login.html', {'tab': 'signup'})

            if password != password2:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'scheduler/login.html', {'tab': 'signup'})

            if User.objects.filter(email=email).exists():
                messages.error(request, 'An account with this email already exists.')
                return render(request, 'scheduler/login.html', {'tab': 'signup'})

            username = email.split('@')[0]
            # make username unique
            base, suffix = username, 1
            while User.objects.filter(username=username).exists():
                username = f"{base}{suffix}"
                suffix  += 1

            parts = full_name.split(' ', 1)
            user  = User.objects.create_user(
                username   = username,
                email      = email,
                password   = password,
                first_name = parts[0],
                last_name  = parts[1] if len(parts) > 1 else '',
            )
            login(request, user)
            messages.success(request, f'Welcome, {user.first_name}! Account created successfully.')
            return redirect('index')

        else:
            # ── Login ────────────────────────────────────────
            email_or_roll = request.POST.get('username', '').strip()
            password      = request.POST.get('password', '')

            # Try email lookup first, then direct username
            user = None
            if '@' in email_or_roll:
                try:
                    u    = User.objects.get(email=email_or_roll)
                    user = authenticate(request, username=u.username, password=password)
                except User.DoesNotExist:
                    pass
            if user is None:
                user = authenticate(request, username=email_or_roll, password=password)

            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', 'index'))
            else:
                messages.error(request, 'Invalid credentials. Please try again.')
                return render(request, 'scheduler/login.html', {'tab': 'login'})

    return render(request, 'scheduler/login.html', {'tab': 'login'})


def logout_view(request):
    logout(request)
    return redirect('landing')


@login_required(login_url='/login/')
def index(request):
    return render(request, 'scheduler/index.html')


@login_required(login_url='/login/')
def generate(request):
    file_path = os.path.join('data', 'dataset.csv')
    data      = load_data_from_csv(file_path)
    scheduled, score = generate_timetable(custom_data=data)
    timetable = timetable_to_dict(scheduled)
    return render(request, 'scheduler/timetable.html', {
        'timetable': timetable,
        'score':     score,
    })
