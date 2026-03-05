from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("seller", "Seller"),
        ("buyer", "Buyer"),
    )

    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    preferred_language = models.CharField(max_length=5, default="en")


class Property(models.Model):

    PROPERTY_TYPES = (
        ("apartment", "Apartment"),
        ("house", "House"),
        ("land", "Land"),
        ("commercial", "Commercial"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)

    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    price = models.DecimalField(max_digits=12, decimal_places=2)
    area = models.FloatField()

    rooms = models.IntegerField(null=True, blank=True)

    floor = models.IntegerField(null=True, blank=True)
    total_floors = models.IntegerField(null=True, blank=True)

    condition = models.CharField(max_length=100)

    image = models.ImageField(upload_to="properties/")

    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews_written"
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews_received"
    )
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)