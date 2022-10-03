from django.shortcuts import render
from django.shortcuts import render, redirect
from wallet.models import Customer
from wallet.models import Wallet
from wallet.models import Account
from wallet.models import Receipt
from wallet.models import Card
from wallet.models import Transaction

from .forms import CustomerRegistrationForm,WalletRegistrationForm,AccountRegistrationForm,TransactionRegistrationForm,ReceiptRegistrationForm,LoanRegistrationForm,RewardRegistrationForm,NotificationRegistrationForm,ThirdPartyRegistrationForm,CardRegistrationForm,Transaction,Receipt,Reward,Loan,Card,ThirdParty,Notification,Account,Wallet


# regestering customers.
def register_customer(request):
    form = CustomerRegistrationForm()
    if request.method =="POST":
        form=(CustomerRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
        else:
            form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{'form':form})

# filtering one customer
def customer_profile(request,id):
    customer=Customer.objects.get(id=id)
    return render(request, "wallet/customer_profile.html", {"customer":customer})

 # displaying list of customers   
def list_customers(request):
    customers=Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"customers":customers})

# editing profile
def edit_profile(request,id):
    customer=Customer.objects.get(id=id)
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST,instance=customer)
        if form. is_valid():
            form.save()
        return redirect("customer_profile", id=customer.id)
    else:
        form =CustomerRegistrationForm(instance=customer)
        return render(request,"wallet/edit_profile.html",{"form":form})
    


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

# filtering one wallet
def wallet_profile(request,id):
    wallet=Wallet.objects.get(id=id)
    return render(request, "wallet/wallet_profile.html", {"wallet":wallet})

# editing profile
def wallet_edit_profile(request,id):
    wallet=Wallet.objects.get(id=id)
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST,instance=wallet)
        if form. is_valid():
            form.save()
        return redirect("wallet_profile", id=wallet.id)
    else:
        form =WalletRegistrationForm(instance=wallet)
        return render(request,"wallet/wallet_edit_profile.html",{"form":form})    
        
    

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

# filtering one wallet
def accounts_profile(request,id):
    account=Account.objects.get(id=id)
    return render(request, "wallet/accounts_profile.html", {"account":account})

# editing profile
def accounts_edit_profile(request,id):
    account=Account.objects.get(id=id)
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST,instance=account)
        if form. is_valid():
            form.save()
        return redirect("accounts_profile", id=account.id)
    else:
        form =AccountRegistrationForm(instance=account)
        return render(request,"wallet/accounts_edit_profile.html",{"account":account})          




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

# filtering one wallet
def transactions_profile(request,id):
    transaction=Transaction.objects.get(id=id)
    return render(request, "wallet/transactions_profile.html", {"transaction":transaction})

# editing profile
def transactions_edit_profile(request,id):
    transaction=Transaction.objects.get(id=id)
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST,instance=transaction)
        if form. is_valid():
            form.save()
        return redirect("transactions_profile", id=transaction.id)
    else:
        form =TransactionRegistrationForm(instance=transaction)
        return render(request,"wallet/transactions_edit_profile.html",{"transaction":transaction})          




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

# filtering one receipts
def receipts_profile(request,id):
    receipt=Receipt.objects.get(id=id)
    return render(request, "wallet/receipts_profile.html", {"receipt":receipt})

# editing profile
def receipts_edit_profile(request,id):
    receipt=Receipt.objects.get(id=id)
    if request.method=="POST":
        form=ReceiptRegistrationForm(request.POST,instance=receipt)
        if form. is_valid():
            form.save()
        return redirect("receipts_profile", id=receipt.id)
    else:
        form =ReceiptRegistrationForm(instance=receipt)
        return render(request,"wallet/receipts_edit_profile.html",{"receipt":receipt})          


def register_loan(request):
    form = LoanRegistrationForm()
    if request.method =="POST":
        form=(LoanRegistrationForm(request.POST))
        if form.is_valid():
            form.save()
        else:
            form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{'form':form}) 

def list_loans(request):
    loans= Loan.objects.all()
    return render(request,"wallet/loans_list.html",{"loans":loans})  


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

# filtering one wallet
def cards_profile(request,id):
    card=Card.objects.get(id=id)
    return render(request, "wallet/cards_profile.html", {"card":card})

# editing profile
def cards_edit_profile(request,id):
    card=Card.objects.get(id=id)
    if request.method=="POST":
        form=CardRegistrationForm(request.POST,instance=card)
        if form. is_valid():
            form.save()
        return redirect("cards_profile", id=card.id)
    else:
        form =CardRegistrationForm(instance=card)
        return render(request,"wallet/cards_edit_profile.html",{"card":card})          



def list_rewards(request):
    rewards= Reward.objects.all()
    return render(request,"wallet/rewards_list.html",{"rewards":rewards}) 


def list_thirdpartys(request):
    thirdpartys= ThirdParty.objects.all()
    return render(request,"wallet/thirdpartys_list.html",{"thirdpartys":thirdpartys})   

def list_notifications(request):
    notifications= Notification.objects.all()
    return render(request,"wallet/notifications_list.html",{"notifications":notifications})  

