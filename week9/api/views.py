from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.http import Http404
from api.models import Products, Category

def to_json(items):
    return [item.to_json() for item in items]

def product_list(request):
    pr_list = Products.objects.all()
    p_json = [product.to_json() for product in pr_list]
    return JsonResponse(p_json, safe=False)

def product_detail(request, id):
    try:
        product = Products.objects.get(id=id)
    except Products.DoesNotExist:
        raise Http404
    return JsonResponse(product.to_json())

def category_list(request):
    ctg_list = Category.objects.all()
    c_json = [category.to_json() for category in ctg_list]
    return JsonResponse(c_json, safe=False)

def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404
    return JsonResponse(category.to_json())

def category_product(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404

    return JsonResponse(to_json(Products.objects.filter(category_id=id)), safe=False)