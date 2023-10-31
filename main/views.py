from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Note
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Main
from .forms import RegisterUserForm, Loginform, CategoryForm, NoteForm
from django.contrib.auth import authenticate, login

class Category_views(TemplateView):
    def home(request):
        if request.user.is_authenticated != True:
            request.endpoint = 'home'
            data = Main.objects.all()
            return render(request, 'main/index.html', {"data": data})
        return redirect('note')

    def note(request):
        if request.user.is_authenticated == True:
            form = CategoryForm()
            data = {
                'form': form,
            }
            return render(request, 'main/note/note.html', data)

    def category_info(request):
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.instance.authors = request.user
                form = form.save()
                return redirect('note')
        if request.user.is_authenticated == True:
            form = CategoryForm()
            data = {
                'form': form
            }
            return render(request, 'main/category/category.html', data)

    def create_category(request):
        if request.method == 'POST':
            form = CategoryForm(request.POST or None)
            if form.is_valid():
                form.instance.authors = request.user
                form.save()
                return redirect('category')
        if request.user.is_authenticated == True:
            forms = CategoryForm()
            return render(request, 'main/category/create_category.html', {'form': forms})

    def delete_category(request, category_id):
        cats = Category.objects.filter(id=category_id)
        cats.delete()
        return redirect("category")

    def edit_category(request, category_id):
        err = ""
        cats = Category.objects.get(id=category_id)
        if request.method == 'POST':
            if "submit" in request.POST:
                if request.POST["category_edit_title"] != '':
                    Category.objects.filter(id=category_id).update(title=request.POST["category_edit_title"])
                    return redirect('category')
                else:
                    err = "Пустое поле"
            elif "exit" in request.POST:
                return redirect('category')
        return render(request, 'main/category/edit_category.html', {'cats': cats, 'err': err})

class Note_views(TemplateView):
    def note_info(request, category_id):
        if request.user.is_authenticated == True:
            note_cats = Note.objects.filter(authors=request.user, category_id_id=category_id)
            cats_title = Category.objects.get(id=category_id).title
            return render(request, 'main/note/detail.html', {'note_cats': note_cats, 'cats_title': cats_title})


    def delete_note(request, note_id, category_id = "main"):
        note = Note.objects.filter(id=note_id)
        note.delete()
        if category_id == "main":
            return redirect('note')
        else:
            return redirect('detail', category_id=category_id)

    def create_note(request):
        category = Category.objects.filter(authors=request.user)
        if request.method == 'POST':
            form = NoteForm(request.POST or None)
            if form.is_valid():
                form.instance.authors = request.user
                form.instance.category_id_id = request.POST['input_note_category']
                form.save()
                return redirect('note')
        if request.user.is_authenticated == True:
            forms = NoteForm()
            return render(request, 'main/note/create_note.html', {'form': forms, 'categorys': category})

    def note_detail(request, note_id):
        note = Note.objects.get(id=note_id)
        cats_title = Category.objects.get(title=note.category_id)
        print(cats_title)
        if request.method == 'POST':
            if "save_edit" in request.POST:
                text = request.POST['note_description']
                Note.objects.filter(id=note_id).update(description=text)
                return redirect('note_detail', note_id)
        return render(request, 'main/note/note_detail.html', {'note': note, 'cats_title': cats_title})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('logins')


def logins(request):
    request.endpoint = 'home'
    form = Loginform(request.POST or None)
    if form.is_valid():
        uservalue = request.POST['username']
        passwordvalue = request.POST['password']

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context = {'form': form}
            return redirect('note')
        else:
            context = {'form': form, 'error': 'Логин/Пароль не правильный'}
            return render(request, 'main/signs.html', context)
    else:
        context = {'form': form}
        return render(request, 'main/signs.html', context)