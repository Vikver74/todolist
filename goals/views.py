from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework import generics, permissions, filters

from goals.models import GoalCategory
from goals.serializers import GoalCategoryCreateSerializer, GoalCategorySerializer


class GoalCategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = GoalCategoryCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class GoalCategoryListAPIView(generics.ListAPIView):
    serializer_class = GoalCategorySerializer
    # queryset = GoalCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['title']
    ordering_fields = ['title', 'created']
    ordering = ['title']
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    def get_queryset(self):
        return GoalCategory.objects.filter(user=self.request.user, is_deleted=False)


class GoalCategoryDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalCategorySerializer
    queryset = GoalCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        return instance
