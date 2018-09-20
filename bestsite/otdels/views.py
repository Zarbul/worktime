from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from workers.models import Worker
from .models import Otdel
from .forms import OtdelsNameForm
from django.utils import timezone
# from ..bestsite import urls


def home(request):
    list_otdels = Otdel.objects.all
    content = {
        # 'title': 'Список рабочих',
        'otdels': list_otdels,
    }
    return render(request, 'otdels/index.html', content)

def detail(request, id=None):
    inst = get_object_or_404(Otdel, id=id)
    worker_list = Worker.objects.all
    content = {
        'id': inst.id,
        'name': inst.name,
        'otdel': worker_list,
    }

    return render(request, 'otdels/detail.html', content)


def new(request, id=None):
    if request.method == "POST":
        formOtdels = OtdelsNameForm(request.POST)
        # formContact = ContactForm(request.POST)
        if formOtdels.is_valid():
            post = formOtdels.save(commit=False)
            post.create_date = timezone.now()
            formOtdels.save()
            # return redirect('detail', id=post.id)
            return redirect('otdels:index')
    else:
        formOtdels = OtdelsNameForm()
        # formContact = ContactForm


    content = {
        'form': formOtdels,
        # 'contact': formContact,
       # 'fname': form.fname,
    }
    return render(request, 'otdels/new.html', content) #{'form': form})



def edit(request, id=None):
    # post = Worker.objects.get(id=id)
    post = get_object_or_404(Otdel, id=id)
    if request.method == "POST":
        form = OtdelsNameForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('otdels:index')
    else:
        form = OtdelsNameForm(instance=post)
    return render(request, 'otdels/edit.html', {'form': form})


def delete(request, id=None):
    post = get_object_or_404(Otdel, id=id)
    post.delete()
    return home(request)