from django.shortcuts import render,redirect
from . models import Expense
from expenseapp.forms import ExpenseForm

# Create your views here.
def index(request):
    if request.method=="POST":
        expense=ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()
    expenses=Expense.objects.all()
    expense_form=ExpenseForm()
    return render(request, 'expenseapp/index.html',{'expense_form':expense_form,'expenses':expenses})

def edit(request,id):
    expense=Expense.objects.get(id=id)
    expense_form=ExpenseForm(instance=expense)
    if request.method=="POST":
        expense=Expense.objects.get(id=id)
        form=ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request,'expenseapp/edit.html',{'expense_form':expense_form})

def delete(request,id):
    if request.method =='POST' and 'delete' in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect('index')