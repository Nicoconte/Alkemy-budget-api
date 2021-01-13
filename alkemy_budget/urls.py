from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alkemy-budget/api/v1/', include('api.users.urls')),
    path('alkemy-budget/api/v1/', include('api.balance.urls')),
    path('alkemy-budget/api/v1/', include('api.operations.urls'))
]
