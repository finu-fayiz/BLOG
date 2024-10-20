from.models import user_signup,Post,ProfilePicture
from django import forms

class user_signupForm(forms.ModelForm):
    class Meta:
        model=user_signup
        fields=['Name','Email','Mobile','Username','Password']
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'Email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'Mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile'}),
            'Username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'Password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            }
        labels={'Name':"",'Email':"",'Mobile':"",'Username':"",'Password':""}

class PostForm(forms.ModelForm): 
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form_control','placeholder':'Title'}),
            'text':  forms.Textarea(attrs={'class':'form_control','placeholder':'text'}),
            'image': forms.ClearableFileInput(attrs={'id': 'myFileInput', 'accept': '.jpg, .png,.gif,.jpeg'}),
        }
        labels={'title':"",'text':""}

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = ProfilePicture
        fields = ['image']
        labels = {
            'image': '',
        }
        widgets = {
            'image': forms.ClearableFileInput(attrs={'id': 'myFileInput','accept': '.jpg, .png, .gif,.jpeg'}),
            }
        
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}),
        label='',
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
        label='',
    )


class Edit_UserForm(forms.ModelForm):
    class Meta:
        model = user_signup
        exclude = ['Password']  # Exclude the 'Password' field from the form
        widgets ={
            'Name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name' }),
            'Email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'Mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile'}),
            'Username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
          
 }