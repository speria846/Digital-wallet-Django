from django.urls import path
from .views import register_customer,register_wallet,register_account,register_transaction,register_receipt,register_loan,register_reward,register_notification,register_thirdparty,register_card,list_customers,list_accounts,list_receipts,list_loans,list_rewards,list_notifications,list_thirdpartys,list_cards,list_wallets,list_transactions,customer_profile,edit_profile,wallet_profile,wallet_edit_profile,accounts_profile,accounts_edit_profile,transactions_edit_profile, transactions_profile,receipts_edit_profile,receipts_profile,cards_profile,cards_edit_profile

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
    path("customers/",list_customers, name='customers_list'),
    path("accounts/",list_accounts, name='accounts_list'),
    path("transactions/",list_transactions, name='transactions_list'),
    path("reciepts/",list_receipts, name='receipts_list'),
    path("loans/",list_loans, name='loans_list'),
    path("rewards/",list_rewards, name='rewards_list'),
    path("notifications/",list_notifications, name='notifications_list'),
    path("thirdpartys/",list_thirdpartys, name='thirdpartys_list'),
    path("cards/",list_cards, name='cards_list'),
    path("wallets/",list_wallets, name='wallets_list'),

    path("one/<int:id>/", customer_profile,name="customer_profile"),
    path("Customers/edit/<int:id>/", edit_profile,name="edit_profile"),

    path("wallets/<int:id>/", wallet_profile,name="wallet_profile"),
    path("Wallets/edit/<int:id>/", wallet_edit_profile, name="wallet_edit_profile"),
    

    path("accounts/<int:id>/", accounts_profile,name="accounts_profile"),
    path("Accounts/edit/<int:id>/", accounts_edit_profile, name="accounts_edit_profile"),
    
    path("transactions/<int:id>/", transactions_profile,name="transactions_profile"),
    path("Transactions/edit/<int:id>/", transactions_edit_profile, name="transactions_edit_profile"),

    path("cards/<int:id>/", cards_profile,name="cards_profile"),
    path("Cards/edit/<int:id>/", cards_edit_profile, name="cards_edit_profile"),


    path("receipts/<int:id>/", receipts_profile,name="receipts_profile"),
    path("Receipts/edit/<int:id>/", receipts_edit_profile, name="receipts_edit_profile"),






]