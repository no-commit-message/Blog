from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', "password1", "password2")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.save()
        return user