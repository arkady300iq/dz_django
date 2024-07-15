from django.shortcuts import render
from myapp.models import Product, Review

def product_list(request):
    products = Product.objects.all()
    return render (request, 'product_list.html', {'products': products})


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        rating = request.POST.get('rating')
        
        if author and text and rating:
            review = Review(product=product, author=author, text=text, rating=rating)
            review.save()
    return render(request, 'product_details.html', {
        'product': product,
        'reviews': reviews,
    })
