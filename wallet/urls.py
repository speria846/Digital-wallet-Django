from django.urls import path
from .views import register_customer,register_wallet,register_account,register_transaction,register_receipt,register_loan,register_reward,register_notification,register_thirdparty,register_card,list_customers,list_accounts,list_transactions,list_reciepts,list_loans,list_rewards,list_notifications,list_thirdpartys,list_cards

urlpatterns = [
    path("register/",register_customer,name='registrations'), 
    path("regwallet/",register_wallet,name='registrations'),
    path("regaccount/",register_account,name='registrations'),
    path("regtransaction/",register_transaction,name='registrations'),
    path("regtreceipt/",register_receipt,name='registrations'),
    path("regloan/",register_loan,name='registrations'),
    path("regreward/",register_reward,name='registrations'),
    path("regnotification/",register_notification,name='registrations'),
    path("regthirdparty/",register_thirdparty,name='registrations'),
    path("regcard/",register_card,name='registrations'),
    path("customers/",list_customers, name='customer_list'),
    path("accounts/",list_accounts, name='account_list'),
    path("transactions/",list_transactions, name='transaction_list'),
    path("reciepts/",list_reciepts, name='reciept_list'),
    path("loans/",list_loans, name='loan_list'),
    path("rewards/",list_rewards, name='reward_list'),
    path("notifications/",list_notifications, name='notification_list'),
    path("thirdpartys/",list_thirdpartys, name='thirdparty_list'),
    path("cards/",list_cards, name='card_list'),


]