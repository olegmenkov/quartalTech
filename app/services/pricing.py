import os


def calculate_price(area, rooms, floor, total_floors, district, underground) -> float:
    scaler_path = 'app/services/data/scaler.pkl'
    model_path = 'app/services/data/model.pkl'
    district_clusters_path = 'app/services/data/district_clusters.pkl'
    underground_clusters_path = 'app/services/data/underground_clusters.pkl'
    """
    Функция для предсказания стоимости квартиры.

    Параметры:
    - area: площадь квартиры (float).
    - floor: этаж квартиры (int).
    - rooms: количество комнат (int).
    - total_floors: общее количество этажей в доме (int).
    - district: район (str).
    - underground: станция метро (str).
    - scaler_path: путь к сохраненному StandardScaler (str).
    - model_path: путь к сохраненной модели (str).
    - district_clusters_path: путь к файлу со словарем кластеров районов (str).
    - underground_clusters_path: путь к файлу со словарем кластеров станций метро (str).
    
    Возвращает:
    - Прогнозируемую стоимость квартиры (float).
    """
    import numpy as np
    import pickle
    import joblib

    # Загрузка словарей кластеров
    with open(district_clusters_path, 'rb') as f:
        cluster_to_districts = pickle.load(f)
    district_clusters = {district: cluster for cluster, districts in cluster_to_districts.items() for district in districts}

    with open(underground_clusters_path, 'rb') as f:
        cluster_to_undergrounds = pickle.load(f)
    underground_clusters = {underground: cluster for cluster, undergrounds in cluster_to_undergrounds.items() for underground in undergrounds}

    # Загрузка scaler и модели
    scaler = joblib.load(scaler_path)
    model = joblib.load(model_path)
    
    # Поиск кластеров для района и метро
    district_cluster = district_clusters.get(district)
    if district_cluster is None:
        # Определение кластера с наибольшим числом районов
        district_cluster = max(cluster_to_districts.items(), key=lambda x: len(x[1]))[0]

    underground_cluster = underground_clusters.get(underground)
    if underground_cluster is None:
        # Определение кластера с наибольшим числом станций метро
        underground_cluster = max(cluster_to_undergrounds.items(), key=lambda x: len(x[1]))[0]

    # Подготовка данных для предсказания
    input_data = np.array([[area, floor, rooms, total_floors, district_cluster, underground_cluster]])
    input_data_scaled = scaler.transform(input_data)
    
    # Предсказание
    predicted_price = model.predict(input_data_scaled)[0]
    return predicted_price
