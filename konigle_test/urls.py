from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from unity.views import BuyerIndex, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BuyerIndex.as_view(), name='buyer_index'),
    path('login/', LoginView.as_view(), name='seller_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='unity/logout.html'), name='seller_logout'),
    path('api/', include('api.urls', namespace='api')),
    path('dashboard/', include('unity.urls', namespace='unity')),
]
