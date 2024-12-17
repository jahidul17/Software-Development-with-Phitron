from django.shortcuts import render
from posts.models import Post
from categories.models import Brand

def home(request, category_slug=None):
    data=Post.objects.all()
    if category_slug is not None:
        brand=Brand.objects.get(slug = category_slug)
        data=Post.objects.filter(brand = brand)
    categories=Brand.objects.all()
    
    return render(request,'home.html', {'data': data, 'brands': categories})