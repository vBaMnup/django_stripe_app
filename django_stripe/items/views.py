import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    """ Страница успешного выполнения операции """
    template_name = 'success.html'


class CancelView(TemplateView):
    """ Страница отмены операции """
    template_name = 'cancel.html'


class ItemCheckoutPageView(TemplateView):
    """ Страница покупки товара """
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super(ItemCheckoutPageView, self).get_context_data(**kwargs)
        context.update({
            'item': Item.objects.get(id=self.kwargs['id']),
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(View):

    def get(self, request, *args, **kwargs):
        """ Получение id сессии """
        item = Item.objects.get(id=kwargs.get('id'))

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": item.price,
                        "product_data": {
                            "name": item.name,
                        },
                    },
                    "quantity": 1,
                },
            ],
            mode='payment',
            success_url=request.headers.get('Referer'),
            cancel_url=request.headers.get('Referer'),
        )

        return JsonResponse({
            'session_id': checkout_session.get('id')
        })
