from django.shortcuts import render, get_object_or_404, loader
from .models import Category, Item
from django.http import HttpResponse
from django.template import RequestContext

def home(request):
    return render(request,'home.html')

def authorize(request):
        return render(request, 'authorize.html')

def login(request):
        #give a form to the template
        return render(request, 'login.html')

def register_as(request):
        # <form method='post'>
        #         {% csrf_token %}
        #         {{form.as_p}}

        #         <input type='submit' name='Create user'/>
 
        # </form>
        return render(request, 'register_as.html')

def item_list(request, category_slug=None):
    template = loader.get_template('catalog.html')
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)

    context = {
                'category': category,
                'categories': categories,
                'items': items
        }

    return HttpResponse(template.render(context))



def item_detail(request, id, slug):
    template = 'Shop/item/detail.html'
    item = get_object_or_404(Item,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                template,
                {'item': item})