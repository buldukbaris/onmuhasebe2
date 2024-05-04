# trendyol_api.py

from django.conf import settings
import base64
import requests

def get_orders(start_date, end_date, page_index, page_size):
    api_key = settings.TRENDYOL_API_SETTINGS['API_KEY']
    secret_key = settings.TRENDYOL_API_SETTINGS['SECRET_KEY']
    supplier_id = settings.TRENDYOL_API_SETTINGS['SUPPLIER_ID']

    url = f'https://api.trendyol.com/sapigw/suppliers/{supplier_id}/orders'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {base64.b64encode(f"{api_key}:{secret_key}".encode()).decode()}',
    }

    params = {
        'startDate': start_date,
        'endDate': end_date,
        'pageIndex': int(page_index),
        'pageSize': int(page_size),
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': response.text}
