from django.urls import path

from items.views import (ItemCheckoutPageView, CancelView, SuccessView,
                         CreateCheckoutSessionView)

urlpatterns = [
    path('item/<id>/', ItemCheckoutPageView.as_view(), name='checkout-page'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path(
        'buy/<id>/',
        CreateCheckoutSessionView.as_view(),
        name='create-checkout-session'
    ),
]
