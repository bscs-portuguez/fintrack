from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib import messages
from django.http import JsonResponse
from .models import DynamicRow
import json

def index(request):
    rows = DynamicRow.objects.all()
    all_columns = set()
    for row in rows:
        all_columns.update(row.data.keys())
    all_columns = sorted(list(all_columns))
    return render(request, 'dynamic_table.html', {
        'rows': rows,
        'columns': all_columns,
    })

def update_row(request, row_id):
    if request.method == 'POST':
        row = get_object_or_404(DynamicRow, id=row_id)
        new_data = {}
        for key in request.POST:
            if key.startswith('col_'):
                col_name = key[4:]
                new_data[col_name] = request.POST[key]
        row.data = new_data
        row.save()
        return JsonResponse({'success': True})

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

# Registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'login.html')

# Welcome page after login
def welcome(request):
    return render(request, 'welcome.html')

def encode(request):
    return render(request, 'encode.html')
