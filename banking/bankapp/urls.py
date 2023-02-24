from django.urls import path
from . import views
app_name = 'bankapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('content/', views.RestrictedView.as_view(), name='content'),
    path('success/', views.success, name='success')

]