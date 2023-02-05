from django.shortcuts import render
from .models import Members
from .serializers import MembersSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class MemberList(ListAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

class MemberCreate(CreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

# Create your views here.
class MemberRetrieve(RetrieveAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

# Create your views here.
class MemberUpdate(UpdateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

# Create your views here.
class MemberDestroy(DestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

# Create your views here.
class MemberListCreate(ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

# Create your views here.
class MemberRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

# Create your views here.
class MemberRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

class MemberRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer