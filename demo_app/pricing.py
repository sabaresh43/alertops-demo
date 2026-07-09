def apply_percentage_discount(price: float, percentage: float) -> float:
    """Return the price after applying a percentage discount."""
    return round(price - (price * percentage / 100), 2)
