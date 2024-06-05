from django.views.generic import TemplateView

from company.models import Company
from products.models import Product

from .models import Slide

# Create your views here.


class HomepageView(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = Slide.objects.all()
        context['company'] = Company.objects.first()

        products = Product.objects.all()
        for product in products:
            product.category_display = product.get_category_display()
        context['products'] = products
        return context
