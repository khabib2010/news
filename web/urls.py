
from django.contrib import admin
from django.urls import path
from news.views import *
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path("create_category/",createCategory,name='createCategory'),
    path('user_register/',user_register,name='user_register'),
    path("news/create/",createNews,name='create_news'),
    path('detail/<int:id>/', detail, name='detail'),
    path('edit/<int:id>/',editnews,name='editnews'),

    
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('delet/<int:id>',delet,name='delet')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

