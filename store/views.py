from django.shortcuts import render, redirect
from .models import Product, ProductCategory
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages


def category_summary(request):
    return render(request, "category_summary.html", {})


def category(request, category_title):
    # replace Hyphens with spaces
    category_title = category_title.replace("-", " ")
    try:
        category = ProductCategory.objects.get(name=category_title)
        products = Product.objects.filter(category=category)
        return render(
            request, "category.html", {"products": products, "category": category}
        )
    except ProductCategory.DoesNotExist:
        messages.error(request, "Category does not exist")
        return render(request, "home.html", {})


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def about(request):
    return render(request, "about.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect("home")
        else:
            messages.success(request, "Login Failed")
            return redirect("login")
    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect("home")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("home")
        else:
            messages.success(request, "Registration Failed")
            return redirect("register")
    else:
        return render(request, "register.html", {"form": form})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {"product": product})
