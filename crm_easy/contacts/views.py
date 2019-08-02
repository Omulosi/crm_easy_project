from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from diango.shortcuts import get_object_or_404

from .models import Contact
from .forms import ContactForm
from ..accounts.models import Account


@login_required
def contact_detail(request, uuid):

    contact = Contact.objects.get(uuid=uuid)

    return render(request, 
                  'contacts/contacts_detail.html',
                  {'contact': contact})


@login_required()
def contact_cru(request, uuid=None, account=None):
    
    if uuid:
        contact = get_object_or_404(Contact, uuid=uuid)
        if contact.owner != request.user:
            return HttpResponseForbidden()
    else:
        contact = Contact(owner=request.user)
    
    if request.POST:
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            # make sure the user owns the account
            account = form.cleaned_data['account']
            if account.owner != request.user:
                return HttpResponseForbidden()
            # save the data
            form.save()
            # return the user to the account detail view

            if request.is_ajax():
                return render(request,
                              'contacts/contact_item_view.html',
                              {'account': account, 'contact': contact})
            else:
                reverse_url = reverse(
                    'crmapp.accounts.views.account_detail',
                    args=(account.uuid,)
                )
                return HttpResponseRedirect(reverse_url)
        else:
            # if the form isn't valid, still fetch the account so it can be passed to the template
            account = form.cleaned_data['account']
    else:
        form = ContactForm()

    if request.GET.get('account', ''):
        account = Account.objects.get(id=request.GET.get('account', ''))

    context = {
        'form': form,
        'contact': contact,
        'account': account
    }

    if request.is_ajax():
        template = 'contacts/contact_item_form.html'
    else:
        template = 'contacts/contact_cru.html'

    return render(request, template, context)
