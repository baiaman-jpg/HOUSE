from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .models import Property, Review
from .serializers import PropertySerializer, ReviewSerializer
from .filters import PropertyFilter


class PropertyViewSet(viewsets.ModelViewSet):

    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filterset_class = PropertyFilter

    search_fields = ["title", "city"]

    ordering_fields = ["price", "created_at"]


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer