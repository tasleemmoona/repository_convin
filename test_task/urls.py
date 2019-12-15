from django.urls import path
from test_task import views

urlpatterns = [
	path('',views.index,name='index'),
]