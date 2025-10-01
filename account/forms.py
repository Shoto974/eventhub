from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from account.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = "user"
        if commit:
            user.save()
        return user