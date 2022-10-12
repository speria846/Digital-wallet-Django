from django.urls import path, include
from rest_framework import routers
from .views import CustomerViewSet
from .views import WalletViewSet
from .views import AccountViewSet
from .views import CardViewSet
from .views import TransactionViewSet
from .views import LoanViewSet
from .views import ReceiptViewSet
from .views import NotificationViewSet

router=routers.DefaultRouter()
router.register("customers",CustomerViewSet)
urlpatterns=[
    path("", include (router.urls)),
]


router=routers.DefaultRouter()
router.register("wallets",WalletViewSet)
urlpatterns=[
    path("", include (router.urls)),
]

router=routers.DefaultRouter()
router.register("accounts",AccountViewSet)
urlpatterns=[
    path("", include (router.urls)),
]

router=routers.DefaultRouter()
router.register("cards",CardViewSet)
urlpatterns=[
    path("", include (router.urls)),
]

router=routers.DefaultRouter()
router.register("transactions",TransactionViewSet)
urlpatterns=[
    path("", include (router.urls)),
]

router=routers.DefaultRouter()
router.register("loans",LoanViewSet)
urlpatterns=[
    path("", include (router.urls)),
]

router=routers.DefaultRouter()
router.register("receipts",ReceiptViewSet)
urlpatterns=[
    path("", include (router.urls)),
]

router=routers.DefaultRouter()
router.register("notifications",NotificationViewSet)
urlpatterns=[
    path("", include (router.urls)),
]
