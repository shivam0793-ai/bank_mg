from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('Home/',views.Home,name='Home'),
    path('create_account/',views.create_account_view,name='create_account'),
    path('MoneyTransfer/',views.MoneyTransfer_view,name='MoneyTransfer'),
    path('success/',views.success,name='success'),
    path('viewstatement/',views.viewstatement,name='viewstatement'),
    path('depost_money',views.depost_money,name='depost_money'),
    path('withdraw_balance',views.withdraw_balance,name='withdraw_balance'),
    path('loan_view',views.loan_view,name='loan_view'),
    path('help_view',views.help_view,name='help_view')
]