from django.urls import path
from .views import *
from .user_views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:test_id/ready_to_test>', ready_to_test, name='ready_to_test'),
    path('<int:test_id/test>', test, name='test'),
    path('signup', signup, name='signup'),
]