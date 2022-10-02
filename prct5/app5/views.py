from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.template import loader
from .models import Employees
from django.contrib import messages
def index(request):
    return render(request, 'app5/home.html' )


def all_emp(request):
    emps = Employees.objects.all()
    contex = {
        'emps':emps
    }
    print(contex)
    return render(request, 'app5/view_all_emp.html',contex)


def add_emp(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        salary = request.POST.get('salary')
        phone = request.POST.get('phone')
        Email = request.POST.get('Email')
        country = request.POST.get('country')
        new_emp = Employees(first_name=first_name,last_name=last_name,middle_name=middle_name,salary=salary,phone=phone,Email=Email,country=country)
        new_emp.save()
        return HttpResponse('Employee added successfully')
    elif request.method=='GET':
        return render(request,'app5/add_emp.html')
    else:
        return HttpResponse('An Exception Occured1 Employee')


def delete_emp(request, id):
    delt = Employees.objects.get(pk=id)
    delt.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    # return redirect('xorstack_app/home.html')
    return render(request,'app5/deleted_suc.html')



def update(request, id):
    mymember = Employees.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))




def updaterecord(request, id):
    first_name = request.POST['first_name']
    middle_name = request.POST['middle_name']
    last_name = request.POST['last_name']
    salary = request.POST['salary']
    phone = request.POST['phone']
    Email = request.POST['Email']
    country = request.POST['country']

    member = Employees.objects.get(id=id)
    member.firs_name = first_name
    member.middle_name = middle_name
    member.last_name = last_name
    member.salary = salary
    member.phone = phone
    member.Email = Email
    member.country = country
    member.save()
    return render(request, 'app5/upd.html')