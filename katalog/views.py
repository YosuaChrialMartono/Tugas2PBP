from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'item_catalog': data_barang_katalog,
    'nama': 'Yosu'
    }
    return render(request, "katalog.html", context)
