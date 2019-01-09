import pytest
from checkout import Checkout


@pytest.fixture
def checkout():
    checkout = Checkout()
    checkout.addPrice("a", 1)
    checkout.addPrice("b", 2)
    return checkout


def test_can_add_an_item(checkout):
    checkout.addItem("a")


def test_calculate_total(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1


def test_calculate_total_multi_items(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3


def test_apply_discount_rule(checkout):
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addDiscount("a", 3, 2)
    assert checkout.calculateTotal() == 2


def test_exception_if_item_has_not_price(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")