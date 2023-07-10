from django.shortcuts import render
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
    return render(request,'expenseapp/edit.html',{'expense_form':expense_form})