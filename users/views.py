from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display empty register form
        form = UserCreationForm()
    else:
        # Processing of filled in form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Enter and redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Otput emty or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
