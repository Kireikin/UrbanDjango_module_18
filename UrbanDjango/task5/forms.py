from django import forms


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, label='Ваше имя:')
#     email = forms.EmailField(label='Email:')
#     message = forms.CharField(widget=forms.Textarea, label='Сообщение:')
#     subscribe = forms.BooleanField(required=False, label='Подписаться на рассылку')


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(min_length=8, max_length=30, label='Введите пароль:', widget=forms.PasswordInput)
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль:', widget=forms.PasswordInput)
    age = forms.CharField(max_length=3, label='Введите свой возраст:')


    # def clean_repeat_password(self):
    #     check_pass = self.cleaned_data
    #     if check_pass['password'] != check_pass['repeat_password']:
    #         raise forms.ValidationError("Passwords don't match.")
    #     return check_pass['repeat_password']
