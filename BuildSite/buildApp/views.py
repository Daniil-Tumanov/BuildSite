from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages

from buildApp.forms import AuthUserForm

from buildApp.models import Service, Category, Feedback

from buildApp.forms import OrderForm, FeedbackForm

from buildApp.models import Orders


def index(request):
    return render(request, 'buildApp/index.html')


def about(request):
    return render(request, 'buildApp/about.html')


def pageNotFound(request, exception):
    return render(request, 'buildApp/404.html')


def showService(request, service_slug):
    form = OrderForm(request.POST or None)
    service = get_object_or_404(Service, Slug=service_slug)
    context = {
        'service': service,
        'title': service.NameService,
        'form': form
    }
    return render(request, 'buildApp/show.html', context=context)


def showCategory(request, category_id):
    category = Category.objects.filter(id=category_id)
    context = {
        'category': category
    }

    return render(request, 'buildApp/category.html', context=context)


def service(request):
    service = Service.objects.all()
    category = Category.objects.all()
    return render(request, 'buildApp/service.html', {"service": service, "category": category})


def contacts(request):
    return render(request, 'buildApp/contacts.html')


def order(request):
    orders = Orders.objects.filter(User=request.user)
    return render(request, 'buildApp/order.html', {"orders": orders})


def feedback(request):
    form = FeedbackForm(request.POST or None)
    return render(request, 'buildApp/feedback.html', {'form': form})


def makeFeed(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST or None)
        if form.is_valid():
            feedback = Feedback()
            feedback.TextFeedback = form.cleaned_data['TextFeedback']
            feedback.File = form.cleaned_data['File']
            feedback.User = User(request.user.id)
            feedback.save()
            messages.success(request, 'Спасибо за Ваше обращение. Мы с Вами свяжемся ')
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/feedback')


class Logout(LogoutView):
    next_page = reverse_lazy('index')


class BuildLoginView(LoginView):
    template_name = 'buildApp/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('index')


def registerPage(request):
    if request.method == 'POST':
        user = User()
        user.first_name = request.POST.get("FirstName")
        user.last_name = request.POST.get("LastName")
        user.email = request.POST.get("Email")
        user.username = request.POST.get("Login")
        user.set_password(request.POST.get("Password"))
        user.save()
        messages.success(request, f"Регистрация успешно завершена. Здравствуйте,"
                    f" {user.first_name} {user.last_name}! Добро пожаловать")
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        next_page = reverse_lazy('index')
        return render(request, 'buildApp/index.html')


def makeOrder(request, id):
    if request.method == 'POST':
        form = OrderForm(request.POST or None)
        service = get_object_or_404(Service, id=id)
        if form.is_valid():
            order = Orders()
            order.Comment = form.cleaned_data['Comment']
            order.Phone = form.cleaned_data['Phone']
            order.User = User(request.user.id)
            order.Service = service
            order.save()
            messages.success(request, 'Ваш заказ успешно оформлен. Ожидайте звонка менеджера')
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/service/')
