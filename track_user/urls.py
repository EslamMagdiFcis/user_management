from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('server-level-var/', views.user_resources, name='server-level-var'),
    path('accounts/', include('django.contrib.auth.urls'))
]
