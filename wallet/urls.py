from django.urls import path
from .views import register_customer,register_wallet,register_account,register_transaction,register_receipt,register_loan,register_reward,register_notification,register_thirdparty,register_card

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

]