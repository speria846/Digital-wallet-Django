from django.shortcuts import render
from wallet.models import Customer
from wallet.models import Account
from .forms import CustomerRegistrationForm,WalletRegistrationForm,AccountRegistrationForm,TransactionRegistrationForm,ReceiptRegistrationForm,LoanRegistrationForm,RewardRegistrationForm,NotificationRegistrationForm,ThirdPartyRegistrationForm,CardRegistrationForm,Transaction,Receipt,Reward,Loan,Card,ThirdParty,Notification,Account,Wallet


# Create your views here.
def register_customer(request):
    form = CustomerRegistrationForm()
    if request.method =="POST":
        form=(CustomerRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
        else:
            form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{'form':form})
    
def list_customers(request):
    customers=Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"customers":customers})
    

def register_wallet(request):
    form = WalletRegistrationForm()
    if request.method =="POST":
        form=(WalletRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
        else:
            form=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{'form':form}) 

def list_wallets(request):
    wallets= Wallet.objects.all()
    return render(request,"wallet/wallets_list.html",{"wallets":wallets})    
    

def register_account(request):
    form = AccountRegistrationForm()
    if request.method =="POST":
        form=(AccountRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
        else:
            form=AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{'form':form}) 

def list_accounts(request):
    accounts= Account.objects.all()
    return render(request,"wallet/accounts_list.html",{"accounts":accounts})    


def register_transaction(request):
    form = TransactionRegistrationForm()
    if request.method =="POST":
        form=(TransactionRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
        else:
            form=TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{'form':form})   

def list_transactions(request):
    transactions= Transaction.objects.all()
    return render(request,"wallet/transactions_list.html",{"transactions":transactions})   

def register_receipt(request):
    form = ReceiptRegistrationForm()
    if request.method =="POST":
        form=(ReceiptRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
        else:
            form=ReceiptRegistrationForm()
    return render(request,"wallet/register_receipts.html",{'form':form}) 

def list_receipts(request):
    receipts= Receipt.objects.all()
    return render(request,"wallet/receipts_list.html",{"receipts":receipts})    


def register_loan(request):
    form = LoanRegistrationForm()
    if request.method =="POST":
        form=(LoanRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
        else:
            form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{'form':form}) 

def register_reward(request):
    form = RewardRegistrationForm()
    if request.method =="POST":
        form=(RewardRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
        else:
            form=RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{'form':form}) 

def register_notification(request):
    form = NotificationRegistrationForm()
    if request.method =="POST":
        form=(NotificationRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
        else:
            form=NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html",{'form':form})   

def register_thirdparty(request):
    form = ThirdPartyRegistrationForm()
    if request.method =="POST":
        form=(ThirdPartyRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
        else:
            form=ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",{'form':form}) 

def register_card(request):
    form = CardRegistrationForm()
    if request.method =="POST":
        form=(CardRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
        else:
            form=CardRegistrationForm()
    return render(request,"wallet/register_card.html",{'form':form}) 

def list_cards(request):
    cards= Card.objects.all()
    return render(request,"wallet/cards_list.html",{"cards":cards})  

def list_loans(request):
    loans= Loan.objects.all()
    return render(request,"wallet/loans_list.html",{"Loan":loans})  

def list_rewards(request):
    rewards= Reward.objects.all()
    return render(request,"wallet/rewards_list.html",{"rewards":rewards}) 


def list_thirdpartys(request):
    thirdpartys= ThirdParty.objects.all()
    return render(request,"wallet/thirdpartys_list.html",{"thirdpartys":thirdpartys})   

def list_notifications(request):
    notifications= Notification.objects.all()
    return render(request,"wallet/notifications_list.html",{"notifications":notifications})  

