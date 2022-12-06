import django_filters
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework import generics, permissions, filters

from goals.filters import GoalFilter, GoalCommentFilter
from goals.models import GoalCategory, Goal, Status, GoalComment
from goals.serializers import GoalCategoryCreateSerializer, GoalCategorySerializer, GoalCreateSerializer, \
    GoalSerializer, GoalCommentCreateSerializer, GoalCommentSerializer


class GoalCategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = GoalCategoryCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class GoalCategoryListAPIView(generics.ListAPIView):
    serializer_class = GoalCategorySerializer
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


class GoalCategoryDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalCategorySerializer
    queryset = GoalCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        return instance


class GoalCreateAPIView(generics.CreateAPIView):
    serializer_class = GoalCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class GoalListAPIView(generics.ListAPIView):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    search_fields = ['title']
    ordering_fields = ['priority', 'due_date']
    ordering = ['-priority', 'due_date']

    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = GoalFilter

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user).exclude(status=Status.archived)


class GoalDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):
        instance.status = Status.archived
        instance.save()
        return instance


class GoalCommentCreateAPIView(generics.CreateAPIView):
    serializer_class = GoalCommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class GoalCommentListAPIView(generics.ListAPIView):
    serializer_class = GoalCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    ordering_fields = ['goal', 'created', 'updated']
    ordering = ['-created']

    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = GoalCommentFilter

    def get_queryset(self):
        # return GoalComment.objects.filter(user=self.request.user, goal=self.request.GET.get('goal'))
        return GoalComment.objects.filter(user=self.request.user)


class GoalCommentDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GoalComment.objects.filter(user=self.request.user)
