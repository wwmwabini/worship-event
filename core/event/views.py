from django.shortcuts import render, redirect
from django.contrib import messages


from .forms import RegistrationForm
from .models import Registration

# Create your views here.
def event_home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            fields = form.cleaned_data
            try:
                registration = Registration(
                    first_name=fields['first_name'],
                    last_name=fields['last_name'],
                    email=fields['email'],
                    phone=fields['phone'],
                    worship_type=fields['worship_type'],
                    payment_transaction=fields['payment_transaction'],
                    payment_number=fields['payment_number'],
                )
                registration.save()
                messages.success(request, 'Thank you for registering. Your payment is being verified. You will receive a confirmation email shortly.')
            except Exception as e:
                messages.error(request, f'An error occurred during registration: {e}')
            return redirect(f"{request.path}#contact")
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")
                return redirect(f"{request.path}#contact")
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'event/home.html', context=context)