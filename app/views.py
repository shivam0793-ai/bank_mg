from django.shortcuts import render,redirect
from app.forms import signUp_form,login_form
from django.contrib.auth.decorators import login_required
from .models import create_account_model,Transaction_History_moduel
import random
from .forms import create_account_form,MoneyTransfer,depost_form,withdraw_balance_form



def index(request):
    context = {
        'login_form': login_form(),
        'register': signUp_form()
    }
    return render(request, 'app/index.html', context)

@login_required
def Home(request):
    user_data=create_account_model.objects.filter(user=request.user).first()
    balance=0
    if user_data:
            balance=user_data.balance
    user_existance=create_account_model.objects.filter(user=request.user).exists()
    obj_data=create_account_model.objects.filter(user=request.user).first()
    return render(request,'app/Home.html',
                  context=
                  {
                      'user_existance':user_existance,
                      'current_balance':balance,
                      'obj_data':obj_data,
                      'depost_data':depost_form(),
                      'withdraw_balance':withdraw_balance_form()
                    })

def deposit(request):
    if request.method=='POST':
        form=depost_form(request.POST)
        if form.is_valid():
            user=create_account_model.objects.get(user=request.user)
            user.balance=form.cleaned_data['amount']
            user.save()
            return redirect('Home')


def generate_account_number():
    while True:
        ac_number=str(random.randint(100000000000, 999999999999))
        if not create_account_model.objects.filter(account_number=ac_number).exists():
            return ac_number

def create_account_view(request):
    if request.method=='POST':
        form=create_account_form(request.POST)
        if form.is_valid():
            account=form.save(commit=False)
            account.user=request.user
            account.account_number=generate_account_number()
            account.save()
            return redirect('Home')
    return render(request,'app/create_account.html',{'form':create_account_form()})





def MoneyTransfer_view(request):

    if request.method == 'POST':

        form = MoneyTransfer(request.POST,request=request)
        if form.is_valid():
            sender = create_account_model.objects.get(
                user=request.user
            )
            receiver = create_account_model.objects.get(account_number=form.cleaned_data['receiver_account'])
            sender.balance -= form.cleaned_data['amount']
            receiver.balance += form.cleaned_data['amount']
            Transaction_History_moduel.objects.create(sender_acc=sender.account_number,reciver_acc=form.cleaned_data['receiver_account'],
            ammount=form.cleaned_data['amount'])
            sender.save()
            receiver.save()
            return redirect('success')
    else:
        form = MoneyTransfer(request=request)
    return render(request, 'app/MoneyTransfer.html', {
        'form': form
    })


def success(request):
    return render(request,'app/success.html')




def viewstatement(request):
    sen=create_account_model.objects.get(user=request.user)
    viewstatement_data=Transaction_History_moduel.objects.filter(sender_acc=sen.account_number)
    return render(request,'app/viewstatement.html',{'viewstatement':viewstatement_data})





def depost_money(request):
    if request.method=='POST':
        form=depost_form(request.POST)
        if form.is_valid():
            user=create_account_model.objects.get(user=request.user)
            user.balance+=form.cleaned_data['amount']
            user.save()
            return redirect('Home')
            


def withdraw_balance(request):
    if request.method=='POST':
       form=withdraw_balance_form(request.POST)
       if form.is_valid():
            user=create_account_model.objects.get(user=request.user)
            if user.balance>=form.cleaned_data['amount']:
                user.balance-=form.cleaned_data['amount']
                user.save()
                return redirect('Home')        


def loan_view(request):
    return render(request,'app/loan.html')


def help_view(request):
    return render(request,'app/help.html')

def signup(request):
    if request.method == 'POST':
        form = signUp_form(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            user.username = " ".join(username.split()).strip().lower()

            user.set_password(form.cleaned_data['password1'])
            user.save()

            print("USER CREATED ✔:", user.username)

            return redirect('login')

        else:
            print("SIGNUP ERROR ❌:", form.errors)

    return redirect('index')