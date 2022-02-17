from django.urls import path
from .views import *

app_name = 'blogposts'

urlpatterns = [
    path('', blogpost_list_view, name='blogpost-list'),
    path('create/', blogpost_create_view, name='blogpost-create'),
    path('<int:id>/', blogpost_detail_view, name='blogpost-detail'),
    path('<int:id>/delete/', blogpost_delete_view, name='blogpost-delete'),
]