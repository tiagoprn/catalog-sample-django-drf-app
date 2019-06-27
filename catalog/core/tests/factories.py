from datetime import datetime

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText, FuzzyChoice, FuzzyDecimal
from core.models import (
    Pants,
    PantsSizes,
    MODEL_CHOICE_FIELD,
    MATERIAL_CHOICE_FIELD,
    SIZE_CHOICE_FIELDS
)


class PantsFactory(DjangoModelFactory):
    class Meta:
        model = Pants

    brand = FuzzyText(length=20)
    model = FuzzyChoice(choices=MODEL_CHOICE_FIELD)
    color = FuzzyText(length=20)
    material = FuzzyChoice(choices=MATERIAL_CHOICE_FIELD)
    cost_price = FuzzyDecimal(low=0)
    sell_price = FuzzyDecimal(low=0)
    profit = FuzzyDecimal(low=0)
    taxes = FuzzyDecimal(low=0)
    is_active = True
    created = datetime.now()
    updated = datetime.now()


class PantsSizesFactory(DjangoModelFactory):
    class Meta:
        model = PantsSizes

    pants = SubFactory(PantsFactory)
    size = FuzzyChoice(choices=SIZE_CHOICE_FIELDS)
    created = datetime.now()
    updated = datetime.now()
