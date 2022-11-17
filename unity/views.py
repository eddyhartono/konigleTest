from datetime import date
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist

from .forms import LoginForm
from api.models import emailList

this_month = date.today().month

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'unity/login.html'
    redirect_authenticated_user = True

def BuyerIndex(request):
    template_name = 'unity/index.html'
    context = {'title': 'Welcome Buyer'}
    return render(request, template_name, context)

def _emailList(request):
    try:
        email_list = emailList.objects.filter(subscribe = True).order_by('-date_action')
        total_subs_this_month = emailList.objects.filter(subscribe = True, date_action__month = this_month).order_by('-date_action')
        total_unsubs = emailList.objects.filter(subscribe = False).order_by('-date_action')
    except ObjectDoesNotExist:
        email_list = None
        total_subs_this_month = 0
        total_unsubs = None

    return email_list, total_subs_this_month, total_unsubs

def _paginator(request, *args):     
    page = Paginator(*args, 25)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)

    return page_obj

@login_required(login_url="seller_login")
def SellerDashboard(request):
    email_list, total_subs_this_month, total_unsubs = _emailList(request)
    page_obj  =  _paginator(request, email_list)
    
    template_name = 'unity/dashboard.html'
    context = { 'title' : 'Dashboard for Seller',
                'email_list' : email_list,
                'total_subs_this_month' : total_subs_this_month,
                'total_unsubs' : total_unsubs,
                'page_obj' : page_obj,
                }
    return render(request, template_name, context)

@login_required
def SellerAllEmail(request):
    email_list, total_subs_this_month, total_unsubs = _emailList(request)
    page_obj  =  _paginator(request, email_list)
    
    template_name = 'unity/partials/all_list.html'
    context = { 'title' : 'Dashboard for Seller',
                'page_obj' : page_obj,
                'email_list' : email_list
                }
    return render(request, template_name, context)

@login_required
def SellerNewSubs(request):
    email_list, total_subs_this_month, total_unsubs = _emailList(request)
    page_obj  =  _paginator(request, total_subs_this_month)
    
    template_name = 'unity/partials/new_subs.html'
    context = { 'title' : 'Dashboard for Seller',
                'page_obj' : page_obj,
                'total_subs_this_month' : total_subs_this_month
                }
    return render(request, template_name, context)

@login_required
def SellerUnsubs(request):
    email_list, total_subs_this_month, total_unsubs = _emailList(request)
    page_obj  =  _paginator(request, total_unsubs)
    
    template_name = 'unity/partials/unsubscribe.html'
    context = { 'title' : 'Dashboard for Seller',
                'page_obj' : page_obj,
                'total_unsubs' : total_unsubs
                }
    return render(request, template_name, context)