from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from accounts.forms import SignUpForm
from django.urls import reverse_lazy

# Create your views here.
@login_required
def accounts(request):
    return render(request, 'registration/account.html')

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')