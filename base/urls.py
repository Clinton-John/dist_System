from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views


urlpatterns = [
    ###Basic Website functionalities
    path('', views.home , name="home"),
    path('home/', views.home , name="home"),
    path('signup/', views.signup , name="signup"),
    path('login/', views.loginPage , name="login"),
    path('logout/', views.logoutPage , name="logout"),

    path('addDetails/', views.addDetails , name="add_details"),


      #email configuration and password reset section
    path('resetPassword/', auth_views.PasswordResetView.as_view(template_name='base/password_reset.html'), name="reset_password" ),
    path('resetPasswordSent/', auth_views.PasswordResetDoneView.as_view(template_name='base/password_reset_sent.html'),name="password_reset_done" ),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='base/password_reset_form.html'), name="password_reset_confirm"),
    path('resetPasswordComplete/', auth_views.PasswordResetCompleteView.as_view(template_name='base/password_reset_done.html'),name="password_reset_complete"),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)