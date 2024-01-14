from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from api_services import views


router = routers.DefaultRouter()
router.register(r'housing', views.HousingView, 'housing')

# router.register(r'restaurants', views.RestaurantView, 'restaurants')
# router.register(r'coworkings', views.CoworkingView, 'coworkings')
# router.register(r'localconsumes', views.LocalConsumeView, 'localconsumes')
# router.register(r'hotels', views.HotelsView, 'hotels')
# router.register(r'form', views.FormView, 'form')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

