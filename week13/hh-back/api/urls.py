from django.urls import path
from api.views.views_fbv import *
from api.views.views_cbv import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', companies),
    path('companies/<int:c_id>', CompanyInfoAPIView.as_view()),
    path('companies/<int:c_id>/vacancies/', vs_by_company),
    path('vacancies/', VacanciesAPIView.as_view()),
    path('vacancies/<int:v_id>/', VacancyDetailAPIView.as_view())
]
