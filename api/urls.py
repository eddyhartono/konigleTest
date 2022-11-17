from django.urls import path
from . import views as api_views

app_name = 'api'

urlpatterns = [
    path('list/', api_views.EmailList.as_view(), name='email_list'),
    path('add/', api_views.EmailCreate.as_view(), name='email_add'),
    path('detail/<int:id>', api_views.EmailDetail.as_view(), name='email_detail'),
]
