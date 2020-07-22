
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

import requests
import pandas as pd

card = Card.where(name='Diabolic Tutor').all()
for card in card:
    print(card.cmc)
