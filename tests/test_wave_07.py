import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest_returns_true():
    pass

def test_swap_by_newest_from_my_empty_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Item(age=1)
    item_e = Item(age=5)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) is 0
    assert len(jolie.inventory) is 2
    assert result is False
    
def test_swap_by_newest_from_their_empty_returns_false():
    item_a = Item(age=1)
    item_b = Item(age=2)
    item_c = Item(age=3)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jolie = Vendor(
        inventory=[]
    )

    result = fatimah.swap_first_item(jolie)

    assert len(fatimah.inventory) is 3
    assert len(jolie.inventory) is 0
    assert result is False

def test_swap_by_newest_returns_true():
    item_a = Item(age=1)
    item_b = Item(age=2)
    item_c = Item(age=3)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age=1)
    item_e = Item(age=5)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) is 3
    assert item_a not in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) is 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_a in jolie.inventory
    assert result is True