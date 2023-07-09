from django.shortcuts import render

from expenseapp.forms import ExpenseForm

# Create your views here.
def index(request):
    expense_form=ExpenseForm()
    return render(request, 'expenseapp/index.html',{'expense_form':expense_form})