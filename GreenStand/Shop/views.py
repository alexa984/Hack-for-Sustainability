from django.shortcuts import render, get_object_or_404
from .models import Category, Item

def home(request):
    return render(request,'home.html')

def item_list(request, category_slug=None):
    template = 'Shop/item/list.html'
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)
        return render(request,
            template,
            {'category': category,
            'categories': categories,
            'items': items})

def item_detail(request, id, slug):
    template = 'Shop/item/detail.html'
    item = get_object_or_404(Item,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                template,
                {'item': item})