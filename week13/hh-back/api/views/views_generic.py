from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer

class CompaniesAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
