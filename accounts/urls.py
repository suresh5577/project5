from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('signup/', views.SignUp.as_view(), name='signup'),
    url('send_mail',views.sendEmail,name='send_mail'),
    url('forget_password',views.forgetPassword, name="forget_password"),
]
