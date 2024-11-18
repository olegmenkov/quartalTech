from app.models import Apartment


def filter_apartments(query, filters):
    if filters.get("min_area"):
        query = query.filter(Apartment.area >= filters["min_area"])
    if filters.get("max_price"):
        query = query.filter(Apartment.estimated_price <= filters["max_price"])
    return query
