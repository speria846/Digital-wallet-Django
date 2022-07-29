from django.contrib import admin
from .models import Customer
from .models import Account
from .models import Wallet
from .models import Transaction
from .models import Card
from .models import ThirdParty
from .models import Notification
from .models import Reciept
from .models import Loan
from .models import Reward

class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","Address",)
    search_fields=("first_name","last_name",)
     
admin.site.register(Customer, CustomerAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_name","account_number","balance",)
    search_fields=("account_name","account_number","balance",)
     
admin.site.register(Account, AccountAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=("status","balance","pin",)
    search_fields=("satus","balance","pin",)
     
admin.site.register(Wallet, WalletAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("amount","number","date",)
    search_fields=("amount","number","date",)
     
admin.site.register(Transaction, TransactionAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display=("card_name","card_number","date",)
    search_fields=("card_name","card_number","date",)
     
admin.site.register(Card, CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display=("name","currency","amount",)
    search_fields=("name","currency","amount",)
     
admin.site.register(ThirdParty, ThirdPartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("title","message","date",)
    search_fields=("title","message","date",)
     
admin.site.register(Notification, NotificationAdmin)

class RecieptAdmin(admin.ModelAdmin):
    list_display=("reciept_type","file","date",)
    search_fields=("reciept_type","file","date",)
     
admin.site.register(Reciept, RecieptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_amount","loan_intrest","due_date",)
    search_fields=("loan_amount","loan_intrest","due_date",)
     
admin.site.register(Loan, LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=("reward_reciepient","amount","date",)
    search_fields=("reward_reciepient","amount","date",)
     
admin.site.register(Reward, RewardAdmin)

