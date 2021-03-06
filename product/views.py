from rest_framework import viewsets
from rest_framework_saasy import viewsets as viewsets_saasy
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets_saasy.ViewSetMixin, viewsets.ModelViewSet):
    """Core product viewset"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        if self.saas_url_kw:
            return Product.objects.filter(merchant__slug=self.saas_url_kw)
        return self.queryset
