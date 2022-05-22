import os

import requests
from bs4 import BeautifulSoup
from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings

from scrape_product.models import ProductImage

logger = get_task_logger(__name__)


@shared_task(name='product_scraping')
def product_scraping(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")
    products = soup.find_all('span', attrs={'images-two'})

    product_image = []
    image_path = settings.IMAGE_SAVE_PATH
    num = 1
    for tag in products:
        link = 'https:' + tag.img['data-srcset']
        image_size = '300px'
        alt_data = tag.img['alt']
        product_image.append(ProductImage(scrape_url=url, original_url=link, original_size=image_size, alt_data=alt_data))

        name = 'image' + str(num)
        num += 1
        try:
            with open(image_path + name + '.jpg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
        except FileNotFoundError:
            os.mkdir(image_path)
            with open(image_path + name + '.jpg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)

    ProductImage.objects.bulk_create(product_image)
    return 'first_task_done'
