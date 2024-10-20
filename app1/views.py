from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout
from django.http import HttpResponse
from django.views import View
from . import models      
from .form import *
from django.contrib.auth.hashers import make_password,check_password



# Create your views here.

def index(request):
    return render(request,'app1/index.html',{'navbar': 'index'})

def about(request):
    return render(request,'app1/about.html',{'navbar': 'about'})

def blog(request):
    return render(request,'app1/blog.html',{'navbar': 'blog'})

# def contact(request):
#     return render(request,'app1/contact.html')

def signup(request):
    form = user_signupForm
    return render(request,'app1/signup.html',{'form':form,'navbar': 'signup'})

class  SignUpViews(View):
    
    def get(self, request):
        form=user_signupForm()
        return render(request,'app1/signup.html',{'form':form,'navbar': 'signup'})
    def post(self, request):
        if request.method == 'POST':
            form=user_signupForm(request.POST, request.FILES)
            if form.is_valid():
                user=form.save(commit=False)      #
                password=form.cleaned_data['Password'] #
                encrypted_password=make_password(password) # password encription
                user.Password=encrypted_password 
                user.save()
                form=user_signupForm()
                context={'msg':'SUCCESSFULLY SIGN UP','form':form}
                return render(request,'app1/signup.html',context)
            else:
                error=form.errors
                return render(request,'app1/signup.html',{'error':error,'form':form})
                
class  SignInViews(View):

    def get(self, request):
        return render(request,'app1/signin.html',{'navbar': 'signin'})
    
    def post(self, request):


        if request.method == 'POST':
            Username = request.POST.get('Username')
            Password=request.POST.get('Password') 
            try:
               user = user_signup.objects.get(Username__exact=Username)
            except user_signup.DoesNotExist:
                user= None
            if user:
                if check_password(Password, user.Password):
                    
                     request.session['Name'] = user.Name
                     request.session['id'] = user.id
                     return render(request, 'app1/index.html')
        return render(request, 'app1/signin.html',{'error':"Invalid username or password"})
    

    
class SignOutView(View):
    def get(self, request):
        your_data = request.session.get('id',None)
        if your_data is not None:
            del request.session['id']
        logout(request)
        return redirect('signin')

class ProfileView(View):
    
    def get(self, request):
        if request.session.get('id'):
            
            form = ProfilePictureForm()
            user_id = request.session['id']
            user =user_signup.objects.get(id=user_id)
            try:
                profile_pic = ProfilePicture.objects.filter(user_id=request.session['id']).values('image').get()
            except ProfilePicture.DoesNotExist:
                profile_pic= None
            if profile_pic:
                context = {'form': form,'user':user,'profile_pic':profile_pic,'menu':'profile','navbar': 'profile'}
            else:
                context = {'form': form,'user':user,'menu':'profile','navbar': 'profile'}


            return render(request, 'app1/profile.html',context)
        else:
            return redirect('signin')
        
    def post(self, request):
        if request.method == 'POST':
            form = ProfilePictureForm(request.POST, request.FILES)
            if form.is_valid():
                user_id = request.session['id']
                profile_pic = ProfilePicture.objects.filter(user_id=user_id).first()
                if profile_pic:
                    profile_pic.image_path = 'uploads/' + request.FILES['image'].name
                    profile_pic.image = request.FILES['image']
                    profile_pic.save()
                    return redirect('profiles')
                else:
                    profile_pic = ProfilePicture()
                    profile_pic.user_id = user_id
                    profile_pic.image_path = 'uploads/' + request.FILES['image'].name
                    profile_pic.image = request.FILES['image']
                    profile_pic.save()
                    return redirect('profile')
            else:
                form = ProfilePictureForm()
    
            return render(request, 'app1/profile.html', {'form': form,'navbar': 'profile'}) 


class EditData(View):
    def get(self, request, id):
        if request.session.get('id'):
            edit_data = get_object_or_404(user_signup, id=id)
            form = Edit_UserForm(instance=edit_data)
            form.fields.pop('Password', None)  # Remove the 'Password' field from the form
            return render(request, 'app1/edit_details.html', {'edit_data': edit_data, 'form': form, 'navbar': 'profiles'})

    def post(self, request, id):
        if request.session.get('id'):
            edit_data = get_object_or_404(user_signup, id=id)
            form = Edit_UserForm(request.POST, instance=edit_data)
            form.fields.pop('Password', None)  # Remove the 'Password' field from the form
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                context = {'msg': 'Profile updated successfully', 'form': form, 'navbar': ''}
                return render(request, 'app1/edit_details.html', context)
            else:
                error = form.errors
                return render(request, 'app1/edit_details.html', {'error': error, 'form': form})
    
    



class ChangePasswordView(View):
    def get(self, request):
        form = ChangePasswordForm()
        return render(request, 'app1/change_pass.html', {'form': form})

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = user_signup.objects.get(id=request.session.get('id'))
            old_password= form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']

            if check_password(old_password, user.Password):
                user.Password = make_password(new_password)
                user.save()
                # messages.success(request, 'Password changed successfully.')
                return redirect('profile')
            else:
                error = "Invalid old password"
                return render(request, 'app1/change_pass.html', {'form': form, 'error': error})
        return render(request, 'app1/change_pass.html', {'form': form})
    


class PostView(View):
    def get(self,request):
        # if request.session.get('id'):
            form=PostForm()
            return render(request,'app1/post.html',{'form':form,'navbar':'post'})
    
    def post(self,request):
        if request.method == 'POST':
            form=PostForm(request.POST,request.FILES)
            if form.is_valid():
                post=form.save(commit=False)
                author_id=request.session['id']
                author=user_signup.objects.get(id=author_id)
                post.author=author
                post.save()
                context={'form':form,'navbar':'post','msg':"post added successfully"}
                return render(request,'app1/post.html',context)  
            else:
                form=PostForm()
                return render(request, 'app1/post.html', {'form':form})
        


class BlogView(View):
    def get(self, request,blog_id=None):
        if blog_id is not None:
            return self.get_blog_detail(request,blog_id)
        blog_f=Post.objects.latest('id')
        blog=Post.objects.exclude(id=blog_f.id).all().order_by('-id')
        context={'navbar':'blog','blog':blog,'blog_f':blog_f}
        return render(request,'app1/blog.html',context,)
        
    
    def get_blog_detail(self,request,blog_id):
        blog=get_object_or_404(Post,id=blog_id)
        context={'navbar':'blog','blog':blog}
        return render(request,'app1/blog_details.html',context)
    
        
    def get_blog_edit(self,request,id):
        blog=get_object_or_404(Post,id=id)
        context={'nvbar':'post','blog':blog}
        return render(request,'app1/post.html',context)


class BlogEditView(View):
    def get(self, request, id):
        blog = get_object_or_404(Post, id=id)
        form = PostForm(instance=blog)
        context={'navbar':'post','form':form, 'blog': blog}
        return render(request, 'app1/post_edit.html', context)
       
    def post(self, request, id):
        blog = get_object_or_404(Post, id=id)
        form = PostForm(request.POST, request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_details', blog_id=blog.id)
        context = {'navbar': 'post', 'form': form, 'blog': blog}
        return render(request, 'app1/post_edit.html', context)


class BlogDeleteView(View):
    def get(self, request, id):
        blog = get_object_or_404(Post, id=id)
        blog.delete()
        return redirect('blog')
