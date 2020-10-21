from django.conf.urls import url
from django.urls import path
 
from . import views
 
app_name = 'form'
urlpatterns = [
    path('',views.feedback_form, name = "home"),
   # url(r'^$', views.feedback_form, name='home'),
    path('feedbacks/',views.feedbacks),
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
]