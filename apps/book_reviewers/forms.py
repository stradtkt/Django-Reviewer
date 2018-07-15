from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=70)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confim_pass = forms.CharField(max_length=100, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class AddBookForm(forms.Form):
    title = forms.CharField(max_length=80)
    content = forms.CharField(widget=forms.Textarea)

class AddReviewForm(forms.Form):
    CHOICES = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'))
    title = forms.CharField(max_length=80)
    body = forms.CharField(max_length=255, widget=forms.Textarea)
    rating = forms.ChoiceField(widget=forms.Select, choices=CHOICES)