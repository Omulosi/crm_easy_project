from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from ..contacts.models import Contact

from .models import Account
from .forms import AccountForm


class AccountList(ListView):
    model = Account
    paginate_by = 2
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        account_search_name = self.request.GET.get('account')
        if account_search_name:
            account_list = Account.objects.filter(
                name__icontains=account_search_name,
                owner=self.request.user
            )
        else:
            account_list = Account.objects.filter(owner=self.request.user)
        return account_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)


@login_required
def account_detail(request, uuid):
    account = Account.objects.get(uuid=uuid)
    if account.owner != request.user:
        return HttpResponseForbidden()

    contacts = Contact.objects.filter(account=account)

    context = {
        'account': account,
        'contacts': contacts,
    }

    return render(request, 'accounts/account_detail.html', context)


@login_required
def account_cru(request, uuid=None):

    if uuid:
        account = get_object_or_404(Account, uuid=uuid)
        if account.owner != request.user:
            return HttpResponseForbidden()
    else:
        account = Account(owner=request.user)

    if request.POST:
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            redirect_url = reverse(
                'accounts:account_detail',
                args=(account.uuid,)
            )
            return HttpResponseRedirect(redirect_url)
    else: 
        form = AccountForm(instance=account)

    context = {
        'form': form,
        'account': account
    }

    if request.is_ajax():
        template = 'accounts/account_item_form.html'
    else:
        template = 'accounts/account_cru.html'
 
    return render(request, template, context)
