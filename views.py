from django.http import HttpResponse

from django.shortcuts import render

from .models import BabySitter
from .forms import BabySitterForm

def index(request):
    babysitter_list = BabySitter.objects.all()
    context = {'babysitter_list': babysitter_list}
    return render(request, 'polls/index.html', context)


def createnew(request):
        if request.method == 'POST':
                form=BabySitterForm(request.POST)
                if form.is_valid():
                bs=form.save(commit=False)
                bs.Name=request.name
                bs.Email=request.email
                bs.Date=request.date
                bs.save()  
                return render(request, 'polls/index.html')  

        else:
                return render(request,'polls/index.html')
