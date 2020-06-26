# chart/modles.py
from django.db import models

class Passenger(models.Model):  # 승객 모델
    # 성별 상수 정의
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )

    # 승선_항구 상수 정의
    CHERBOURG = 'C'
    QUEENSTOWN = 'Q'
    SOUTHAMPTON = 'S'
    PORT_CHOICES = (
        (CHERBOURG, 'Cherbourg'),
        (QUEENSTOWN, 'Queenstown'),
        (SOUTHAMPTON, 'Southampton'),
    )

    name = models.CharField(max_length=100, blank=True)                 # 이름
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)           # 성별
    survived = models.BooleanField()                                    # 생존_여부
    age = models.FloatField(null=True)                                  # 연령
    ticket_class = models.PositiveSmallIntegerField()                   # 티켓_등급
    embarked = models.CharField(max_length=1, choices=PORT_CHOICES)     # 승선_항구

    def __str__(self):
        return self.name

class covid19(models.Model):
    date = models.DateField()
    # france = models.DecimalField(decimal_places=1, max_digits=6)
    # germany = models.DecimalField(decimal_places=1, max_digits=6)
    # korea = models.DecimalField(decimal_places=1, max_digits=6)
    # us = models.DecimalField(decimal_places=1, max_digits=6)
    # uk = models.DecimalField(decimal_places=1, max_digits=6)
    # uk = models.FloatField()
    france = models.FloatField()
    germany= models.FloatField()
    korea = models.FloatField()
    us = models.FloatField()
    uk = models.FloatField()

    def __str__(self):
        return self.date