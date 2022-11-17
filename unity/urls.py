from django.urls import path
from .views import SellerDashboard, SellerNewSubs, SellerUnsubs, SellerAllEmail

app_name = 'unity'

urlpatterns = [
    path('', SellerDashboard, name='dashboard'),
    path('all_list/', SellerAllEmail, name='all_list'),
    path('new_sub/', SellerNewSubs, name='new_subs_list'),
    path('unsubs/', SellerUnsubs, name='unsubs_list'),
]
