from django.shortcuts import render,get_object_or_404,redirect
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.http import Http404
# from django.shortcuts import 
# Create your views here.

@login_required
def employees_view(request):
    employees = Employee.objects.all()
    return render(request,'model/home.html',{'employees':employees})

@login_required
def employee_detail(request,pk):
    try:
        employee = get_object_or_404(Employee,pk=pk)
    except Http404:
        return render(request,'model/not_found.html',status=404)
    return render(request,'model/employee_detail.html',{'employee':employee})

@login_required
def delete_confirmation(request,pk):
    employee = get_object_or_404(Employee,pk=pk)
    return render(request,'model/delete_confirmation.html',{'employee':employee})

@login_required
def delete_employee(request,pk):
    employee = get_object_or_404(Employee,pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('all-employees')
    return redirect('confirm-delete',pk=pk)

@login_required
def create_employee(request):
    if request.method =='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-employees')
    else:
        form = EmployeeForm()
    return render(request,'model/create_employee.html',{'form':form})
    
@login_required
def update_employee(request,pk):
    employee = get_object_or_404(Employee,pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('all-employees')
        return render(request,'model/not_found.html')
    else:
        form=EmployeeForm(instance=employee)
    return render(request,'model/update_employee.html',{'form':form})




def search_view(request):
    query  = request.GET.get('search','').strip()
    employees = Employee.objects.filter(
        Q(first_name__icontains=query)|
        Q(last_name__icontains=query)|
        Q(email__icontains=query)|
        Q(department__dept_name__icontains=query)|
        Q(department__city__icontains=query)
    ) if query else Employee.objects.all()
    
    return render(request,'model/home.html',{'employees':employees,'query':query})