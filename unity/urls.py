from django.urls import path
from .views import SellerNewSubs, SellerUnsubs, SellerAllEmail

app_name = 'unity'

urlpatterns = [
    path('', SellerAllEmail.as_view(), name='all_list'),
    path('new_sub/', SellerNewSubs.as_view(), name='new_subs_list'),
    path('unsubs/', SellerUnsubs.as_view(), name='unsubs_list'),
]
