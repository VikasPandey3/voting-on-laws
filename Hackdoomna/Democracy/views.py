from django.shortcuts import render, HttpResponse, redirect
from .forms import CustomUserCreationForm, VoteForm
from .models import Vote
from django.contrib.auth import authenticate, login
from django.db.models import Q


def index(request):
    return render(request, 'Democracy/index.html')


def signin(request):
    return render(request, 'Democracy/signin.html')


def signupview(request):
    return render(request, 'Democracy/signup.html')


def aboutus(request):
    return render(request, 'Democracy/about.html')


def Services(request):
    return render(request, 'Democracy/services.html')


def blog(request):
    return render(request, 'Democracy/blog.html')


def contact(request):
    return render(request, 'Democracy/contact.html')


def auth_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('Index')

        else:
            return HttpResponse("Sorry! Your account in Permanentaly Dishabled.")
    else:
        return render(request, 'Democracy/signin.html', {'message': 'Invalid Username or password'})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Signin')
        else:
            return HttpResponse("!!Invalid Credential!!<br>"
                                "your password can't be too similar to your other personal information.")


def voting(request):
    return render(request, 'Democracy/voting_portal.html')


def save_response(request):
    if request.method == "POST":
        voter = request.POST["voter"]
        law_code = request.POST['law_code']
        check_obj = Vote.objects.filter(Q(voter=voter) & Q(law_code=law_code))
        if len(check_obj):
            return render(request, "Democracy/voting_portal.html", {"message": "you already voted"})

        else:
            form = VoteForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return render(request, "Democracy/voting_portal.html", {"message": "you vote is recorded"})
            else:
                return render(request, "Democracy/voting_portal.html",
                              {"message": "Something went wrong you vote is not recorded"})
