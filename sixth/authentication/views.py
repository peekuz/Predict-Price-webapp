from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from sklearn.ensemble.gradient_boosting import predict_stage
from sklearn.externals import joblib
import numpy as np
from .forms import PostForm


# Create your views here.


def index(request):
    pred = 0
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Rooms = request.POST.get('Rooms')
            Bathroom = request.POST.get('Bathroom')
            Landsize = request.POST.get('Landsize')
            BuildingArea = request.POST.get('BuildingArea')
            YearBuilt = request.POST.get('YearBuilt')
            values=[Rooms,Bathroom,Landsize,BuildingArea,YearBuilt]
            values= np.array(values).reshape(1,5)
            model = joblib.load('houseprediction.sav')
            pred = int(model.predict(values))
    else:
        form=PostForm()
    context = {'form': form,'prediction' :pred}
    return render(request,'authentication/index.html', context)


def register(request):
    if request.method(request.POST):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()
    
    context={'form':form}
    return render(request, 'registration/register,html', context)




