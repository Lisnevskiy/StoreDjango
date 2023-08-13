from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegForm, UserForm
from users.models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}


class UserLogoutView(LogoutView):
    pass


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegForm
    success_url = reverse_lazy('users:reg_confirmation')
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):
        self.object = form.save()

        verification_url = self.request.build_absolute_uri(
            reverse('users:verify') + f'?key={self.object.verification_key}'
        )

        send_mail(
            subject='Подтверждение электронной почты',
            message=f'Перейдите по ссылке, чтобы подтвердить свой адрес электронной почты: {verification_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )

        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm
    extra_context = {'title': 'Профиль'}

    def get_object(self, queryset=None):
        return self.request.user


def verify(request):
    key = request.GET.get('key')

    try:
        user = User.objects.get(verification_key=key, is_verified=False)
    except User.DoesNotExist:
        raise Http404('Invalid verification key')

    user.is_verified = True
    user.save()

    context = {'title': 'Верификация'}

    return render(request, 'users/verification_success.html', context=context)


def reg_confirmation(request):
    context = {'title': 'Подтверждение регистрации'}
    return render(request, 'users/reg_confirmation.html', context=context)


def reset_password(request):
    context = {'title': 'Сброс пароля'}

    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'users/email_not_found.html', context)

        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()

        message = f'Ваш новы пароль для авторизации {new_password}'
        # send_mail('New Password', message, settings.DEFAULT_FROM_EMAIL, [email])
        send_mail(
            subject='New Password',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )

        return render(request, 'users/new_password.html', context)
    else:
        return render(request, 'users/reset_password.html', context)


def new_password(request):
    context = {'title': 'Новый пароль'}
    return render(request, 'users/new_password.html', context=context)


def email_not_found(request):
    context = {'Не найдено'}
    return render(request, 'users/email_not_found.html', context=context)

