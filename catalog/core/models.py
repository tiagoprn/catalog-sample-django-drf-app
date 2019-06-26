from django.db import models

MODEL_CHOICE_FIELD = [
    ('regular', 'REGULAR'),
    ('skinny', 'SKINNY'),
    ('slim', 'SLIM'),
    ('fit', 'FIT'),
    ('cargo', 'CARGO'),
]

MATERIAL_CHOICE_FIELD = [
    ('jeans', 'JEANS'),
    ('tracksuit', 'TRACKSUIT'),
    ('twill', 'TWILL'),
]

SIZE_CHOICE_FIELDS = [
    ('PP', 'PP'), ('P', 'P'), ('M', 'M'),
    ('G', 'G'), ('GG', 'GG'), ('XG', 'XG'),
    (30, 30), (32, 32), (34, 34),
    (36, 36), (38, 38), (40, 40),
    (42, 42), (44, 44), (46, 46),
    (48, 48), (50, 50), (52, 52),
    (54, 54), (56, 56), (58, 58)
]


class Pants(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20, choices=MODEL_CHOICE_FIELD)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICE_FIELD)
    cost_price = models.DecimalField(max_digits=8, decimal_places=2)
    sell_price = models.DecimalField(max_digits=8, decimal_places=2)
    profit = models.DecimalField(max_digits=8, decimal_places=2)
    taxes = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField()
    created = models.DateTimeField()
    updated = models.DateTimeField()


class PantsSizes(models.Model):
    pants = models.ForeignKey(
        Pants,
        related_name='pants',
        on_delete=models.CASCADE
    )
    size = models.CharField(max_length=2, choices=SIZE_CHOICE_FIELDS)
    is_active = models.BooleanField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['pants', 'size'],
                name='pants_size'
            )
        ]
