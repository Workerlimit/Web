from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Company, Vacancy

def welcome(request):
    return HttpResponse("""<h2>Welcome to HeadHunter</h2>
    <h3>Here you can find a job and we help you</h3>""")

def get_companies(request):
    companies = Company.objects.all()
    comp_json = [comp.to_json() for comp in companies]
    return JsonResponse(comp_json, safe=False)

def get_company(request, c_id):
    try:
        company = Company.objects.get(id=c_id).to_json()
    except Company.DoesNotExist as dne:
        return JsonResponse({'OOPS': str(dne)})
    return JsonResponse(company)

def get_vacancies(request):
    vacancies = Vacancy.objects.all()
    vac_json = [vac.to_json() for vac in vacancies]
    return JsonResponse(vac_json, safe=False)

def get_vacancy(request, v_id):
    try:
        vacancy = Vacancy.objects.get(id=v_id).to_json()
    except Vacancy.DoesNotExist as dne:
        return JsonResponse({'OOPS': str(dne)})
    return JsonResponse(vacancy)

def get_vs_by_company(request, c_id):
    try:
        company = Company.objects.get(id=c_id)
    except Company.DoesNotExist as dne:
        return JsonResponse(company, safe=False)

    vacancies = company.vacancy_set.all()
    v_json = [v.to_json() for v in vacancies]
    return JsonResponse(v_json, safe=False)

def vacancies_top_ten(request):
    top = Vacancy.objects.all().order_by('-salary')[:10]
    top_json = [v.to_json() for v in top]
    return JsonResponse(top_json, safe=False)




