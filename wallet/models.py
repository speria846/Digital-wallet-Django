from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    Address=models.TextField()
    phonenumber=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()

class Account(models.Model):
    account_name=models.CharField(max_length=15)
    account_number=models.IntegerField()
    balance=models.IntegerField() 

class Wallet(models.Model):
    status=models.CharField(max_length=15)
    balance=models.IntegerField()
    pin=models.IntegerField()  

class Transaction(models.Model):
    amount=models.IntegerField()
    number=models.IntegerField()
    date=models.DateTimeField() 


class Card(models.Model):
    card_name=models.CharField(max_length=15)
    card_number=models.IntegerField()
    date=models.DateTimeField()

class ThirdParty(models.Model):
    name=models.CharField(max_length=15)
    currency=models.IntegerField()
    amount=models.IntegerField()    

class Notification(models.Model):
    title=models.CharField(max_length=15)
    message=models.CharField(max_length=15)
    date=models.DateTimeField()      

class Reciept(models.Model):
    reciept_type=models.CharField(max_length=15)
    file=models.FileField()
    date=models.DateTimeField() 

class Loan(models.Model):
    loan_amount=models.IntegerField()
    loan_intrest=models.IntegerField()
    due_date=models.DateTimeField()   

class Reward(models.Model):
    reward_reciepient=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateTimeField() 
          
