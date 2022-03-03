from dataclasses import field
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Moment, Photo
from .serializers import MomentSerializer, PhotoSerializer

# Create your views here.
class MomentCreate( generics.ListCreateAPIView):
    queryset = Moment.objects.all()
    serializer_class = MomentSerializer

class MomentList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moment.objects.all()
    serializer_class = MomentSerializer

class PhotoCreate(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer



# class MomentCreate(LoginRequiredMixin, CreateView):
#     model = Moment
#     fields = '__all__'

# class MomentList(LoginRequiredMixin, ListView):
#     model = Moment

# class MomentDetail(LoginRequiredMixin, DetailView):
#     model = Moment

# class MomentUpdate(LoginRequiredMixin, UpdateView):
#     model = Moment
#     fields = ['title', 'description']

# class MomentDelete(LoginRequiredMixin, DeleteView):
#     model = Moment
#     success_url = '/rotmg/collection/' 

# class PhotoCreate(LoginRequiredMixin, CreateView):
#     model = Photo
#     fields = '__all__'

# class PhotoUpdate(LoginRequiredMixin, UpdateView):
#     model = Photo
#     fields = ['url']

# class PhotoDelete(LoginRequiredMixin, DeleteView):
#     model = Photo
#     success_url = '/rotmg/collection'