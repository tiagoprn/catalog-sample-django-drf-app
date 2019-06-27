from django.db import models

MODEL_CHOICE_FIELD = [
    'regular',
    'skinny',
    'slim',
    'fit',
    'cargo',
]

MATERIAL_CHOICE_FIELD = [
    'jeans',
    'tracksuit',
    'twill',
]

SIZE_CHOICE_FIELDS = [
    'PP', 'P', 'M', 'G', 'GG', 'XG',
    30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60
]


class Pants(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20, choices=MODEL_CHOICE_FIELD)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICE_FIELD)
    cost_price = models.DecimalField(max_digits=8, decimal_places=2)
    sell_price = models.DecimalField(max_digits=8, decimal_places=2)
    profit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    taxes = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.model} - {self.color}'

    def save(self, *args, **kwargs):
        self.profit = self.sell_price - (self.cost_price + self.taxes)
        super().save()


class PantsSizes(models.Model):
    pants = models.ForeignKey(
        Pants,
        related_name='pants_sizes',
        on_delete=models.CASCADE
    )
    size = models.CharField(max_length=2, choices=SIZE_CHOICE_FIELDS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.pants.model} - {self.size}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['pants', 'size'],
                name='pants_size'
            )
        ]
