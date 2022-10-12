from rest_framework import serializers
from wallet.models import Customer
from wallet.models import Wallet
from wallet.models import Account
from wallet.models import Card
from wallet.models import Transaction
from wallet.models import Loan
from wallet.models import Receipt
from wallet.models import Notification



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "email", "age")

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("customer_id", "amount", "date")     

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("account_number", "account_name", "customer")  

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("Card_name", "Expiry_date", "card_number")    

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("transaction_ref", "wallet", "transaction_amount") 

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("transaction_ref", "wallet", "transaction_amount") 

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ("receipt_type", "receipt_date", "transaction")                                            



class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("title", "message", "recipient")   




