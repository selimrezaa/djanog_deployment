from django.conf.urls import url
from django.urls import path
from second_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


app_name = 'second_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
