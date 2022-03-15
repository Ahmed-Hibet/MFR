from django.urls import path
from facility.views import FacilityList, FacilityDetail


urlpatterns = [
    path('', FacilityList.as_view()),
    path('<int:pk>/', FacilityDetail.as_view()),
]
