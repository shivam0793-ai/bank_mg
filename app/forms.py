from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class login_form(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'user_name'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password...'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.strip().lower()

class signUp_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text=""
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if " " in username:
         raise forms.ValidationError("Username cannot contain spaces")
        return username


from .models import create_account_model
class create_account_form(forms.ModelForm):
    class Meta:
        model=create_account_model
        exclude=['account_number','user','created_at']



class MoneyTransfer(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    receiver_account = forms.CharField(max_length=12)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        cleaned_data = super().clean()
        receiver_acc = cleaned_data.get('receiver_account')
        amount = cleaned_data.get('amount')

        if not self.request:
            raise forms.ValidationError("Request not available")

        receiver = create_account_model.objects.filter(account_number=receiver_acc).first()
        if not receiver:
            raise forms.ValidationError("Receiver account does not exist")

        sender = create_account_model.objects.get(user=self.request.user)
        if sender.account_number == receiver_acc:
            raise forms.ValidationError("Cannot transfer to same account")

        if sender.balance < amount:
            raise forms.ValidationError("Insufficient balance")

        return cleaned_data
    
class depost_form(forms.Form):
    amount=forms.DecimalField(max_digits=12,decimal_places=2)



class withdraw_balance_form(forms.Form):
    amount=forms.DecimalField(max_digits=12,decimal_places=2)