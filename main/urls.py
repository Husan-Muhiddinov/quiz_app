from django.urls import path
from .views import *
from .user_views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:test_id>/ready_to_test', ready_to_test, name='ready_to_test'),
    path('<int:test_id>/test', test, name='test'),
    path('<int:checktest_id>/checktest', checktest, name='checktest'),
    path('new_test',new_test, name="new_test"),
    path('<int:test_id>/new_question',new_question, name="new_question"),
    path('signup', signup, name='signup'),
    path('<int:user_id>/profile', profile, name='profile')
]