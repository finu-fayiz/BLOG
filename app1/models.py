from django.db import models

# Create your models here.
class user_signup(models.Model):
    Name=models.CharField(max_length=25)
    Email=models.EmailField(max_length=25, unique=True)
    Mobile=models.CharField(max_length=10, unique=True)
    Username=models.CharField(max_length=25, unique=True)
    Password=models.CharField(max_length=252)

    def _str_(self):
        return self.Name
    

class ProfilePicture(models.Model):
    user = models.OneToOneField(user_signup, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='uploads', null=True, blank=True)

    def _str_(self):
        return f"profile picture for {self.user.Username}"
    
    
class Post(models.Model):
    image = models.ImageField(upload_to='uploadimage', null=True, blank=True)
    title = models.CharField(max_length=220)
    text = models.TextField(max_length=500)
    def _str_(self):
        return self.title