from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Worker
from .forms import WorkerNameForm, ContactForm
from django.shortcuts import redirect
from django.utils import timezone


def home(request):
    list_workers = Worker.objects.all
    content = {
        # 'title': 'Список рабочих',
        'workers': list_workers,
    }
    return render(request, 'index.html', content)


def detail(request, id=None):
    instance = get_object_or_404(Worker, id=id)
    content = {
        'name': instance.name,
        'fname': instance.fname,
        'instance': instance,
    }
    return render(request, 'detail.html', content)



def new(request, id=None):
    if request.method == "POST":
        form = WorkerNameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            form.save()
            return redirect('detail', id=post.id)
    else:
        form = WorkerNameForm()

    #content = {
    #    'name': form.name,
     #   'fname': form.fname,
    #}
    return render(request, 'edit.html', {'form': form})


def edit(request, id=None):
    # post = Worker.objects.get(id=id)
    post = get_object_or_404(Worker, id=id)
    if request.method == "POST":
        form = WorkerNameForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('edit', id=post.id)
    else:
        form = WorkerNameForm(instance=post)
    return render(request, 'edit.html', {'form': form})


