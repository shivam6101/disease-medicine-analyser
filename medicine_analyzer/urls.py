from django.contrib import admin
from django.urls import path,include
from medical import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index,name='index'),
    path('diseas',views.diseas,name='diseas'),
    path('diseas_analyser',views.diseas_analyser,name='diseas_analyser'),
    path('',views.home,name='home'),
    path('create',views.create,name='create'),
    path('image_ocr',views.image_ocr,name='image_ocr'),
    path('camimg',views.camimg,name='camimg'),
    
]
