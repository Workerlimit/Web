from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.serializers import CompanySerializer, VacancySerializer
from api.models import Company, Vacancy

class Companies(generics.ListCreateAPIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'Error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CompanyInfoAPIView(APIView):
    def getting(self, c_id):
        try:
            return Company.objects.get(id = c_id)
        except Company.DoesNotExist as cdne:
            return Response({'Error': str(cdne)})

    def get(self, request, c_id):
        company = self.getting(c_id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, c_id):
        company = self.getting(c_id)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'Error': serializer.errors})

    def delete(self, request, c_id):
        company = self.getting(c_id)
        company.delete()
        return Response({'Deleted': True})

class VacanciesAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'Error': serializer.errors})

class VacancyDetailAPIView(APIView):
    def getting(self, request, v_id):
        try:
            return Vacancy.objects.get(id=v_id)
        except Vacancy.DoesNotExist as vdne:
            return Response({'Error': str(vdne)})

    def get(self, request, v_id):
        vacancy = self.getting(v_id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, v_id):
        vacancy = self.getting(v_id)
        serializer = VacancySerializer(instance=vacancy, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'Error': serializer.errors})

    def delete(self, request, v_id):
        vacancy = self.getting(v_id)
        vacancy.delete()
        return Response({'Deleted': True})