from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'
    verbose_name = "Shop Orders"

    def ready(self):
        import checkout.signals
