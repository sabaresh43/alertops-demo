from demo_app.pricing import apply_percentage_discount


def test_applies_percentage_discount() -> None:
    assert apply_percentage_discount(100, 20) == 80


def test_zero_discount_does_not_change_price() -> None:
    assert apply_percentage_discount(100, 0) == 100

