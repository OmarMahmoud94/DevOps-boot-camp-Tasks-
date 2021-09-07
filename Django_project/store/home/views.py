from django.shortcuts import render,redirect
from .models import Products, Category
from django.http.response import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'home/index3.html')

def view_products(request):
    return render(request, 'home/products.html', {'all_products': Products.objects.all()})

def create_product(request):
    return render(request, 'home/create_product.html', {'all_categories' : Category.objects.all()})

def save_product(request):
    if request.method == 'POST':
        p_name = request.POST.get('product_name')
        p_price = request.POST.get('product_price')
        p_description = request.POST.get('product_description')
        p_photo = request.FILES.get('myfile')
        p_cat = request.POST.get('product_category')

        if p_name == '' or p_price == '' or p_description == '': 
            return HttpResponse('All fields must be filled')
        elif int(p_price) <= 0:
            return HttpResponse('pricd must be greater than 0')
        elif p_description.isdigit():
            return HttpResponse('description must be desciptive. enter text content')

        for product in Products.objects.all():
            if product.name == p_name : 
                return HttpResponse('this book is aleady exist')  

        Products.objects.create(
            name = p_name,
            price = p_price,
            description = p_description,
            photo = p_photo,
            category = Category.objects.get(name=p_cat)
        )

        return redirect('products-page')
 #  return HttpResponse('invalid request')

def edit_product(request, product_id):
    return render(request,  'home/edit.html', 
        {'product_data' : Products.objects.get(pk=product_id), 'all_categories' : Category.objects.all()})
 


def save_edited_product(request, edited_product_id):
    if request.method == 'POST':
        
        edited_product = Products()
        edited_product.id = edited_product_id
        edited_product.name = request.POST.get('product_name')
        edited_product.price = request.POST.get('product_price')
        edited_product.description = request.POST.get('product_description')
        

        if request.FILES.get('myfile'):
            edited_product.photo = request.FILES.get('myfile')
        else:
            edited_product.photo = Products.objects.get(pk=edited_product_id).photo

        print(request.POST.get('product_category'))
        if request.POST.get('product_category'):
            cat_name = request.POST.get('product_category')
            edited_product.category = Category.objects.get(name=cat_name)
        else:
            edited_product.category = Products.objects.get(pk=edited_product_id).category
        
        if edited_product.name == '' or edited_product.price == '' or edited_product.description == '': 
            return HttpResponse('All fields must be filled')
        elif float(edited_product.price) <= 0:
            return HttpResponse('pricd must be greater than 0')
        elif edited_product.description.isdigit():
            return HttpResponse('description must be desciptive. enter text content')


        edited_product.save()
        
        return redirect('products-page')

def delete_product(request,product_id):
    Products.objects.get(pk=product_id).delete()
    return redirect('products-page')