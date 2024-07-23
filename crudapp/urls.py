from django.urls import path
from . import views
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('',views.form_submit, name='form_submit'),
    path('home/',views.home_page,name='home_content'),
    path('collections/',views.collections_page,name='collections_content'),
    path('trends/',views.trends_page,name='trends_content'),
    path('traditional/',views.traditional_page,name='traditional_content'),
    path('contact/',views.contact_page,name='contact_content'),
    path('about/',views.about_page,name='about_content'),
    path('cartList/',views.cartList_page,name='cartList_content'),
    path('images/upload_page/',views.upload_page,name='upload_page_content'),
    
]