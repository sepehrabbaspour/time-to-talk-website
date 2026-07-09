from django.urls import path
from pages.views import *

app_name = 'pages'

urlpatterns = [
path("detail/" , detail_page , name='detail-page'),
path("listing/" , listing_page , name='listing-page'),    

]
