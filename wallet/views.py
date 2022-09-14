from django.shortcuts import render
from wallet.models import Customer
from wallet.models import Account
from .forms import CustomerRegistrationForm,WalletRegistrationForm,AccountRegistrationForm,TransactionRegistrationForm,ReceiptRegistrationForm,LoanRegistrationForm,RewardRegistrationForm,NotificationRegistrationForm,ThirdPartyRegistrationForm,CardRegistrationForm


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


def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{'form':form}) 

def register_account(request):
    form = AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{'form':form})  

def register_transaction(request):
    form = TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{'form':form})     

def register_receipt(request):
    form = ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",{'form':form}) 

def register_loan(request):
    form = LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{'form':form}) 

def register_reward(request):
    form = RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{'form':form}) 

def register_notification(request):
    form = NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html",{'form':form})   

def register_thirdparty(request):
    form = ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",{'form':form}) 

def register_card(request):
    form = CardRegistrationForm()
    return render(request,"wallet/register_card.html",{'form':form}) 

def list_customers(request):
    customers=Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"Customer":customers})

def list_accounts(request):
    accounts= Account.objects.all()
    return render(request,"wallet/accounts_list.html",{"Account":accounts})    

def list_transactions(request):
    transactions= Transaction.objects.all()
    return render(request,"wallet/transactions_list.html",{"Transaction":transactions})   

def list_reciepts(request):
    reciepts= Reciept.objects.all()
    return render(request,"wallet/reciepts_list.html",{"Reciept":reciepts})    

def list_loans(request):
    loans= Loan.objects.all()
    return render(request,"wallet/loans_list.html",{"Loan":loans})  

def list_rewards(request):
    rewards= Reward.objects.all()
    return render(request,"wallet/rewards_list.html",{"Rewards":rewards}) 


def list_thirdpartys(request):
    thirdpartys= ThirdParty.objects.all()
    return render(request,"wallet/thirdpartys_list.html",{"ThirdParty":thirdpartys})   

def list_notifications(request):
    notifications= Notifications.objects.all()
    return render(request,"wallet/notifications_list.html",{"Notifications":notifications})  

def list_cards(request):
    cards= Card.objects.all()
    return render(request,"wallet/cards_list.html",{"Card":cards})  
