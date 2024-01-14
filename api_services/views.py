from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.

class HousingView(viewsets.ModelViewSet):
    serializer_class = HousingSerializer
    queryset = Housing.objects.all()