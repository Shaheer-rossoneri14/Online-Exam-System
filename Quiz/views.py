from django.shortcuts import render, redirect
from .forms import Registration
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Subject, Question

# Create your views here.
@login_required(login_url='home:login')
def home(request):
    sub = Subject.objects.all()

    if request.method == 'POST':
        s = request.POST['cat']
        b = Question.objects.filter(subject__id=s)
        if len(b) != 0:
            return redirect('home:question', s)
        else:
            messages.error(request, 'Question is not set for this subject')
    return render(request,'quiz/home.html', {'subject':sub}, {'user':request.user})

def signup(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            if user is not None:
                if user.is_active:
                    return redirect('home:home')
    else:
        form = Registration()

    return render(request,'quiz/signup.html', {'form':form})

def login(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    else:
        if request.method == 'POST':
            username = request.POST['user']
            password = request.POST['pass']

            try:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_active:
                        dj_login(request, user)
                        return redirect('home:home')
                else:
                    messages.error(request, 'Username and Password not match')
            except ObjectDoesNotExist:
                print("invalid User")
        return render(request, 'quiz/login.html')

@login_required(login_url='home:login')
def question(request, subject_id):
    sub = Subject.objects.get(id=subject_id)
    ques = Question.objects.filter(subject__sub=sub)
    if request.method == 'POST':
        c = (request.POST)
        a=[]
        for q in ques:
            a.append(q.ans)
        l=[]
        for b in c:
            l.append(c[b])

        l.pop(0)
        t = len(a)
        r=0
        w=0
        n=0
        for i in range(t):
            if l[i]=='no_attempt':
                n+=1
            if a[i]==l[i]:
                r+=1
            else:
                w+=1
        at=t-n
        result = int((r*100)/t)
        ans = [r, w, n, at, t, result]

        return render(request,'quiz/answer.html', {'ans': ans})
    return render(request, 'quiz/show_ques.html', {'ques': ques})


def log(request):
    logout(request)
    return redirect('home:login')