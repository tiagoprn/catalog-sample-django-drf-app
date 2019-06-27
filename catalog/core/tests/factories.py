from datetime import datetime

from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText, FuzzyChoice, FuzzyDecimal
from core.models import (
    Pants,
    MODEL_CHOICE_FIELD,
    MATERIAL_CHOICE_FIELD,
)


class PantsFactory(DjangoModelFactory):  # pylint: disable=too-many-ancestors
    class Meta:
        model = Pants

    brand = FuzzyText(length=20)
    model = FuzzyChoice(choices=MODEL_CHOICE_FIELD)
    color = FuzzyText(length=20)
    material = FuzzyChoice(choices=MATERIAL_CHOICE_FIELD)
    cost_price = FuzzyDecimal(low=100, high=499)
    sell_price = FuzzyDecimal(low=500, high=999)
    taxes = FuzzyDecimal(low=1, high=99)
    created = datetime.now()
    updated = datetime.now()
