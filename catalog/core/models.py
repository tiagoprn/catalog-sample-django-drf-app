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


class Pants(models.Model):
    class Meta:
        verbose_name_plural = "Pants"
        unique_together = ('brand', 'model', 'color', 'material')

    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20, choices=MODEL_CHOICE_FIELD)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICE_FIELD)
    cost_price = models.DecimalField(max_digits=8, decimal_places=2)
    sell_price = models.DecimalField(max_digits=8, decimal_places=2)
    profit = models.DecimalField(max_digits=8, decimal_places=2,
                                 blank=True, null=True)
    taxes = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return (f'Pants(brand={self.brand}, '
                f'model={self.model}, '
                f'color={self.color}), '
                f'material={self.material}')

    def __str__(self):
        return self.__repr__()

    def save(self, *args, **kwargs):  # pylint: disable=arguments-differ, unused-argument
        self.profit = self.sell_price - (self.cost_price + self.taxes)
        super().save()
