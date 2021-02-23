from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs with a method named index ")
def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def show(request, number):
    return HttpResponse(f"placeholder to display blog: {number}")
def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}")
def delete(request, number):
    return redirect("/")
def count(request, num):
    context = {
        "number": num
    }
    return render(request, "count.html", context)