from django.urls import path
from . import views
from .views import SignUpViews,SignInViews,BlogDeleteView
from .views import SignOutView,ProfileView,BlogEditView
from .views import ChangePasswordView,EditData,BlogView,PostView


urlpatterns = [
    path('',views.index,name="index"),
    path('blog/',BlogView.as_view(), name='blog'),
    path('post/',PostView.as_view(),name='post'),
    # path('contact',views.contact,name="contact"),
    path('signup',SignUpViews.as_view(),name="signup"),
    path('signin',SignInViews.as_view(),name="signin"),
    path('profile',ProfileView.as_view(),name="profile"),
    path('signout',SignOutView.as_view(),name="signout"),
    path('change_pass/',ChangePasswordView.as_view(),name='change_pass'),
    path('edit_details/<int:id>/',EditData.as_view(),name='edit_details'),
    path('blog_details/<int:blog_id>/',BlogView.as_view(), name='blog_details'),
    path('blog_edit/<int:id>/',BlogEditView.as_view(), name='blog_edit'),
    path('blog_delete/<int:id>/',BlogDeleteView.as_view(), name='blog_delete'),
    ]
