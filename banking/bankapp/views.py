from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    return render(request, "index.html")
# @login_required
# def content(request):
#     return render(request, 'content.html')

class RestrictedView(LoginRequiredMixin, TemplateView):
    template_name = 'content.html'
    raise_exception = True  # Raise exception when no access instead of redirect
    permission_denied_message = "You are not allowed here."

@login_required
def success(request):
    if request.method == 'POST':
        name = request.POST['Name']
        mail = request.POST['mailid']
    return render(request, 'success.html', {'name2': name , 'mail':mail})