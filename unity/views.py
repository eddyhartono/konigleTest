from datetime import date
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from .forms import LoginForm
from api.models import emailList

this_month = date.today().month

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'unity/login.html'
    redirect_authenticated_user = True

class BuyerIndex(TemplateView):
    template_name = 'unity/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Welcome Buyer'
        return context

class ContextMixin(object):
    model = emailList
    paginate_by = 25
    
    def get_context_data(self, **kwargs):
        context = super(ContextMixin, self).get_context_data(**kwargs)
        context["title"] = 'Welcome To Seller Dashboard'
        context["email_list"] = emailList.objects.filter(subscribe = True).order_by('-date_action').count()
        context["total_subs_this_month"] = emailList.objects.filter(subscribe = True, date_action__month = this_month).order_by('-date_action').count()
        context["total_unsubs"] = emailList.objects.filter(subscribe = False).order_by('-date_action').count()
        return context
    
class SellerAllEmail(LoginRequiredMixin,ContextMixin,ListView):
    template_name = 'unity/partials/all_list.html'
    queryset = emailList.objects.filter(subscribe = True).order_by('-date_action')
    
class SellerNewSubs(LoginRequiredMixin,ContextMixin,ListView):
    template_name = 'unity/partials/new_subs.html'
    queryset = emailList.objects.filter(subscribe = True, date_action__month = this_month).order_by('-date_action')

class SellerUnsubs(LoginRequiredMixin,ContextMixin,ListView):
    template_name = 'unity/partials/unsubscribe.html'
    queryset = emailList.objects.filter(subscribe = False).order_by('-date_action')
