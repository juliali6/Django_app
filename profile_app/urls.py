from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from profile_app.views.auth import AuthView
from profile_app.views.logout_profile import LogoutUser
from profile_app.views.profile import ProfileUserView

from profile_app.views.registration import RegistrationView
from profile_app.views.update_profile import UserUpdate


urlpatterns = [
    path('registration', RegistrationView.as_view(), name='reg_page'),
    path('profile/update', login_required(UserUpdate.as_view()), name='update_profile'),
    path('logout', LogoutUser.as_view(), name='logout_page'),
    path('login', AuthView.as_view(), name='login_page'),
    path('profile/', login_required(ProfileUserView.as_view()), name='profile_page'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
