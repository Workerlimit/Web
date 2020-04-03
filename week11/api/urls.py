from django.urls import path
from api.views import get_companies, get_company, get_vacancies, get_vacancy, get_vs_by_company, vacancies_top_ten

urlpatterns = [
    path('companies/', get_companies),
    path('companies/<int:c_id>', get_company),
    path('companies/<int:c_id>/vacancies/', get_vs_by_company),
    path('vacancies/', get_vacancies),
    path('vacancies/<int:v_id>/', get_vacancy),
    path('vacancies/top10/', vacancies_top_ten)
]
