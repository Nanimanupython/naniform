from django.shortcuts import render

from .forms import EmployeeForm
from .models import FormsData
from django.http import HttpResponse
def employee_details(request):
    if request.method == 'POST':
        eform = EmployeeForm(request.POST)
        if eform.is_valid():
            first_name = request.POST.get('first_name')
            second_name = request.POST.get('second_name')
            salary = request.POST.get('salary')
            address = request.POST.get('address')
            data = FormsData(
                first_name=first_name,
                second_name=second_name,
                salary=salary,
                address=address,
            )
            data.save()
            eform = EmployeeForm()
            return render(request,'employee.html',{'eform':eform})
        else:
            return HttpResponse('invalid form')
    else:
        eform = EmployeeForm()
        return render(request,'employee.html',{'eform':eform})


