from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render_to_response, HttpResponseRedirect, render
import datetime
from .models import *
from .forms import ContactForm, SignUpForm


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render_to_response(html)


def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body> In %s hour(s), the date and time would be: %s </body></html>" % (offset, dt)
    return render_to_response(html)


def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(email__contains=query) |
            Q(fullName__contains=query)
        )
        results = SignUp.objects.filter(qset).distinct()
    else:
        results = []

    return render_to_response("search.html", {"results": results, "query": query})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data.get('topic')
            message = form.cleaned_data.get('message')
            sender = form.cleaned_data.get('sender', 'noreply@example.com')
            send_mail('Feedback to Your site , topic: %s' %topic, message, sender,
                      ['vidasaboktakin@gmail.com'])
            html = "<html><body>ThankYou</body></html>"
            return HttpResponseRedirect(html)
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})


def sign_up_view(request):
    form = SignUpForm(request.POST or None)
    Context = {'form': form}
    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("fullName")
        if not full_name:
            full_name = "viiviids"
            instance.fullName = full_name
        instance.save()
    return render(request, 'sign_up.html', Context)




