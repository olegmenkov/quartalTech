from app.services import analytics, filters, pricing

def test_analytics_service(setup_test_db):
    trends = analytics.analyze_price_trends(setup_test_db)
    assert trends["trends"] == "prices are rising"

def test_filters_service(setup_test_db):
    min_area = 30
    area_min_aparts = filters.filter_apartments(setup_test_db, area_min=min_area)
    assert all(a.area > min_area for a in area_min_aparts)

    max_area = 30
    area_max_aparts = filters.filter_apartments(setup_test_db, area_max=max_area)
    assert all(a.area < max_area for a in area_max_aparts)

    min_rooms = 2
    rooms_min_aparts = filters.filter_apartments(setup_test_db, rooms_min=min_rooms) 
    assert all(a.rooms > min_rooms for a in rooms_min_aparts)

    max_rooms = 3
    rooms_max_aparts = filters.filter_apartments(setup_test_db, rooms_max=max_rooms) 
    assert all(a.rooms < max_rooms for a in rooms_max_aparts)

    min_price = 10_000_000
    price_min_aparts = filters.filter_apartments(setup_test_db, price_min=min_price) 
    assert all(a.estimated_price > min_price for a in price_min_aparts)

    max_price = 5_000_000
    price_max_aparts = filters.filter_apartments(setup_test_db, price_max=max_price) 
    assert all(a.estimated_price < max_price for a in price_max_aparts)

    no_aparts = filters.filter_apartments(setup_test_db, max_price=1_000_000, min_price=20_000_000)
    assert len(no_aparts) == 0

def test_pricing_service(setup_test_db):
    price = pricing.calculate_price(15.1, 1)
    assert price == 10_000_000

