from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    # If form is submitted (POST request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():  # regex validation done here
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user against Django's database
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # If authentication successful
                login(request, user)
                return redirect('accounts:success')
            else:
                # If username/password doesn't match database
                form.add_error(None, "Invalid username or password.")
    else:
        # If page is opened initially (GET request)
        form = LoginForm()

    # Render the login page with the form
    return render(request, 'accounts/login.html', {'form': form})


def success_view(request):
    # Show success message after login
    return render(request, 'accounts/success.html')
