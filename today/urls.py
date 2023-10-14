from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.home,name="home"),
    path("signin",views.signin,name='signin'),
    path("signout",views.signout,name='signout'),
    path("signup",views.signup,name="signup"),
    path("profile",views.profile,name="profile"),
    path("resetPassword",views.resetPassword,name="resetPassword")
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)