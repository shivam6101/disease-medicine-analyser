from django.urls import path,include
from . import views
app_name='medical'

urlpatterns = [
    # path('',views.predict,name='predict'),
    # path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('image_ocr',views.image_ocr,name='image_ocr'),
    path('camimg',views.camimg,name='camimg'),
]