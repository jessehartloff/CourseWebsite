from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(label='Comment', max_length=140)

    # def __init__(self):
    #     # super(forms.Form)
    #     self.fields['comment'].widget.attrs.update({'autofocus': 'on'})


# user_name = forms.EmailField(max_length=25)
# password = forms.CharField(widget=forms.PasswordInput, label="password")


# def __init__(self):
#     self.fields['user_name'].widget.attrs.update({'autofocus': 'autofocus'
#                                                                'required': 'required', 'placeholder': 'User Name'})
#     self.fields['password'].widget.attrs.update({
#         'required': 'required', 'placeholder': 'Password'})