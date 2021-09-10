
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'date_of_birth'
        ]

