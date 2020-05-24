from django.shortcuts import render, redirect  
from Scoreboard_app.forms import ScoresForm  
from Scoreboard_app.models import Scores  
# Create your views here.  
def emp(request):  #Emp is used when new player is added to scoreboard. If form is valid, we return to list, if not, nothing happens and error is displayed (see error tags in index.html)
    if request.method == "POST":  
        form = ScoresForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ScoresForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  #Show all scores
    scores = Scores.objects.all()  
    return render(request,"show.html",{'scores':scores})

def ascending(request): #Show all scores in ascending order
    scores = Scores.objects.order_by('Score')  
    return render(request,"show.html",{'scores':scores})

def descending(request): #Show all scores in descending order
    scores = Scores.objects.order_by('-Score')  
    return render(request,"show.html",{'scores':scores})

def destroy(request, id):  #Destroy an object from database
    scores = Scores.objects.get(id=id)  
    scores.delete()  
    return redirect("/show")  