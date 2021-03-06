from django.urls import path

from scrape_product.views import ScrapeProductAPIView, ProductDetailsAPIView

urlpatterns = [
    path('internal/v1/scrape-product/',
         ScrapeProductAPIView.as_view(),
         name='scrape-product-v1-create'),

    path('internal/v1/product-details',
         ProductDetailsAPIView.as_view(),
         name='product-details')

]