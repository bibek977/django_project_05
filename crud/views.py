from django.shortcuts import render,redirect
from .models import Employees

# Create your views here.
def index(request):
    emp = Employees.objects.all()

    context = {
        'emp' : emp
    }
    return render(request, 'crud/index.html', context)

def add(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        new_emp = Employees(
            name=name,
            email=email,
            phone=phone,
            address=address
        )
        new_emp.save()

        return redirect('index')
    return render(request, 'crud/index.html')

def read(request):
    if request.method == "POST":
        emp = Employees.objects.all()
        context = {
            'emp' : emp
        }
        return redirect('index')
    return render(request,'crud/index.html',context)

def update(request, id):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        new_emp = Employees(
            id = id,
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        new_emp.save()

        return redirect("index")
    return render(request, 'crud/index.html')


def delete(request,id):
    emp = Employees.objects.filter(id = id)
    emp.delete()
    return redirect("index")