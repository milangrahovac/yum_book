from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('recepies', views.all_recipes, name='all_recipes'),
    path('recepie/<slug:slug>', views.recepie_detail, name='recipe-detail-page'),
    path('category/<str:selected_category>',
         views.recipes_by_category, name='recipes_by_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
