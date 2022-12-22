import datetime

from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.http import request

from main_app.validator import only_letters_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_letters_validator,
        )
    )
    last_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_letters_validator,
        )
    )

    picture = models.URLField(
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=30,
        choices=(('male', 'male'), ('femail', 'femail'), ('Do not show', 'Do not show')),
        default='Do not show',
        null=True,
        blank=True
    )

    account = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    @property
    def total_likes(self):
        result = 0
        photos_of_profile_pets = PetPhoto.objects.filter(account=self.account)
        if photos_of_profile_pets:
            for p in photos_of_profile_pets:
                result += p.likes
        return result

    def __str__(self):
        return self.first_name


class Pet(models.Model):
    TYPES = [(x, x) for x in ("Cat", "Dog", "Bunny", "Parrot", "Fish", "Other")]
    name = models.CharField('Pet name', max_length=30)
    type = models.CharField(
        max_length=max(len(x) for (x, y) in TYPES),
        choices=TYPES
    )
    date_of_birth = models.DateField(
        'Day of birth',
        null=True,
        blank=True
    )
    account = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('name',)

    def __str__(self):
        return self.name


class PetPhoto(models.Model):
    photo = models.ImageField(
        'Pet image',
        upload_to='pet_photos/',

    )
    tagged_pets = models.ManyToManyField(Pet)
    description = models.TextField(
        null=True,
        blank=True,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0
    )

    account = models.ForeignKey(
        User,
        related_name='account_owner_photo',
        on_delete=models.CASCADE,
        unique=False,
    )

    list_who_like_photo = models.ManyToManyField(
        User,
        related_name='account_liked_photo',
        blank=True,
    )

    def __str__(self):
        result = [x.name for x in self.tagged_pets.all()]
        return ' | '.join(result)
