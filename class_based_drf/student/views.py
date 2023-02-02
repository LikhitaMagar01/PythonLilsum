from django.shortcuts import render
from .models import Kids
from .serializers import KidsSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
# your views here.
# Generic APIView and model Mixin

class KidsList(ListModelMixin, GenericAPIView):
  queryset = Kids.objects.all()
  serializer_class = KidsSerializer
  def get(self, request, *args, **kwargs):
     return self.list(request, *args, **kwargs)

class KidsCreate(CreateModelMixin, GenericAPIView):
  queryset = Kids.objects.all()
  serializer_class = KidsSerializer
  def post(self, request, *args, **kwargs):
     return self.create(request, *args, **kwargs)

class KidsRetrieve(RetrieveModelMixin, GenericAPIView):
  queryset = Kids.objects.all()
  serializer_class = KidsSerializer
  def get(self, request, *args, **kwargs):
     return self.retrieve(request, *args, **kwargs)

class KidsUpdate(UpdateModelMixin, GenericAPIView):
  queryset = Kids.objects.all()
  serializer_class = KidsSerializer
  def put(self, request, *args, **kwargs):
     return self.update(request, *args, **kwargs)

class KidsDelete(DestroyModelMixin, GenericAPIView):
  queryset = Kids.objects.all()
  serializer_class = KidsSerializer
  def delete(self, request, *args, **kwargs):
     return self.destroy(request, *args, **kwargs)

# list and create - pk not required
class listCreateAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Kids.objects.all()
    serializer_class = KidsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RetrieveUpdateDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Kids.objects.all()
    serializer_class = KidsSerializer

    def get(self, request, *args, **kwargs):
     return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
     return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
     return self.destroy(request, *args, **kwargs)
