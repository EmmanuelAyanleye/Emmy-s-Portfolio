from django.contrib import admin
from django.urls import path, include
import portfolio_app
from portfolio_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio_app.urls'))
]
