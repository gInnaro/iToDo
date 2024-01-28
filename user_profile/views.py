from django.shortcuts import render, get_object_or_404, redirect
import random, string
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm


def generator_telegram_key():
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, 16))
    return rand_string



class UserProfile(TemplateView):
    def main(request):
        key = ''
        username = request.user
        if request.method == 'POST':
            if "submit" in request.POST:
                u_form = UserUpdateForm(request.POST, instance=username)
                p_form = ProfileUpdateForm(request.POST, request.FILES, instance=username.profile)
                if u_form.is_valid() and p_form.is_valid():
                    u_form.save()
                    p_form.save()
                    return redirect('user_profile')
            elif "connect-tg" in request.POST:
                key = generator_telegram_key()
                form = ProfileUpdateForm(request.POST, request.FILES, instance=username.profile)
                if form.is_valid():
                    form.instance.tg_key = key
                    form.save()
                return redirect('user_profile')
            elif "user_update" in request.POST:
                u_form = UserUpdateForm(request.POST, instance=username)
                if u_form.is_valid():
                    u_form.save()
                    return redirect('user_profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=username.profile)
        data = {
            'profile': Profile.objects.get(user=username),
            'user': User.objects.get(username=username),
            'p_form': p_form,
            'u_form': u_form,
        }

        return render(request, 'user_profile/user_profile.html', data)
