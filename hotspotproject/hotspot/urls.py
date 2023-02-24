from . import views
from django.urls import path
app_name='hotspot'

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('feature/',views.feature,name='feature'),
    path('add_item/',views.add_item,name='add_item'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]