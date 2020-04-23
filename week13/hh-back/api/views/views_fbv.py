from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import *
from api.models import *

@api_view(['GET', 'POST'])
def companies(request):
    if request.method == 'GET':
        companiess = Company.objects.all()
        serializer = CompanySerializer(companiess, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'Error': serializer.errors})

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, c_id):
    try:
        company = Company.objects.get(id=c_id)
    except Company.DoesNotExist as cdne:
        return Response({'Error': str(cdne)})

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CompanySerializer(company)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'Error': serializer.errors})
    elif request.method == 'DELETE':
        company.delete()
        return Response({'Deleted': True})

@api_view(['GET', 'POST'])
def vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VacancySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'Error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def vacancy_detail(request, v_id):
    try:
        vacancy = Vacancy.objects.get(id=v_id)
    except Vacancy.DoesNotExist as vdne:
        return Response({'Error': str(vdne)})

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        vacancy.delete()
        return Response({'deleted': True})

@api_view(['GET'])
def vs_by_company(request, c_id):
    if request.method == 'GET':
        try:
            company = Company.objects.get(id=c_id)
        except Company.DoesNotExist as cdne:
            return Response({'Error': str(cdne)})

        vacancies= Vacancy.objects.filter(company=company)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
