from django.shortcuts import render, redirect
from .models import Product, ProductCategory, Profile
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        # Query The Products DB Model
        searched = Product.objects.filter(
            Q(name__icontains=searched) | Q(description__icontains=searched)
        )
        # test for null
        if not searched:
            messages.success(
                request, "Could't find what you are looking for, Please try again"
            )
            return render(request, "search.html", {})
        else:
            return render(request, "search.html", {"searched": searched})
    else:
        return render(request, "search.html", {})


def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(id=request.user.id)
        info_form = UserInfoForm(request.POST or None, instance=current_user)

        if info_form.is_valid():
            info_form.save()
            messages.success(request, "Info Updated")
            return redirect("home")

        return render(request, "update_info.html", {"info_form": info_form})

    else:
        messages.success(request, "Login first to access to this page")
        return redirect("login")


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            user_password = ChangePasswordForm(current_user, request.POST)
            if user_password.is_valid():
                user_password.save()
                messages.success(request, "Password Updated Successfully")
                login(request, current_user)
                return redirect("update_user")
            else:
                for error in list(user_password.errors.values()):
                    messages.error(request, error)
                    return redirect("update_password")
        else:
            user_password = ChangePasswordForm(current_user)
            return render(
                request, "update_password.html", {"user_password": user_password}
            )

    else:
        messages.success(request, "Login first to access to this page")
        return redirect("login")


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "Profile Updated")
            return redirect("home")

        return render(request, "update_user.html", {"user_form": user_form})

    else:
        messages.success(request, "Login first to access to this page")
        return redirect("login")


def category_summary(request):
    categories = ProductCategory.objects.all()
    return render(request, "category_summary.html", {"categories": categories})


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
            messages.success(
                request,
                "Account created, Please complete your info to finish registration",
            )
            return redirect("update_info")
        else:
            messages.success(request, "Registration Failed")
            return redirect("register")
    else:
        return render(request, "register.html", {"form": form})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {"product": product})
