from django.shortcuts import render

# Create your views here.

def detail_page(request):
    return render(request , 'pages/detail-page.html')

def listing_page(request):
    return render(request , 'pages/listing-page.html')