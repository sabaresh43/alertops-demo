def apply_percentage_discount(price: float, percentage: float) -> float:
    """Return the price after applying a percentage discount."""
    # Intentional demo defect: the discount is added instead of subtracted.
    return round(price + (price * percentage / 100), 2)

