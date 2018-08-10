from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from .models import Worker
from .forms import WorkerNameForm, ContactForm
from django.utils import timezone
from django.contrib import auth


def home(request):
    list_workers = Worker.objects.all
    content = {
        # 'title': 'Список рабочих',
        'workers': list_workers,
        'username': auth.get_user(request).username,
    }
    return render(request, 'workers/index.html', content)




def detail(request, id=None):
    instance = get_object_or_404(Worker, id=id)
    content = {
        'name': instance.name,
        'fname': instance.fname,
        'instance': instance,
        'otdel': instance.otdel,
        'username': auth.get_user(request).username,
    }
    return render(request, 'workers/detail.html', content)



def new(request, id=None):
    if request.method == "POST":
        formWorker = WorkerNameForm(request.POST)
        formContact = ContactForm(request.POST)
        if formWorker.is_valid():
            post = formWorker.save(commit=False)
            post.create_date = timezone.now()
            formWorker.save()
            # return redirect('detail', id=post.id)
            return redirect('index')
    else:
        formWorker = WorkerNameForm()
        formContact = ContactForm


    content = {
        'form': formWorker,
        'contact': formContact,
       # 'fname': form.fname,
    }
    return render(request, 'workers/new.html', content) #{'form': form})



def edit(request, id=None):
    # post = Worker.objects.get(id=id)
    post = get_object_or_404(Worker, id=id)
    if request.method == "POST":
        form = WorkerNameForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = WorkerNameForm(instance=post)
    return render(request, 'workers/edit.html', {'form': form})


def delete(request, id=None):
    post = get_object_or_404(Worker, id=id)
    post.delete()
    return home(request)


