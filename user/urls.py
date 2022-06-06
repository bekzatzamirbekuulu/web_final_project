from django.contrib import admin
from django.urls import path
from .views import Login, Logout, Registrate

app_name = 'user'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-login/', Login.as_view(), name='login'),
    path('user-logout/', Logout.as_view(), name='logout'),
    path('about-us/', Registrate.as_view(), name='registrate'),
]

