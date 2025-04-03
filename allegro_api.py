import requests

class AllegroAPI:
    def __init__(self, access_token):
        self.base_url = "https://api.allegro.pl/"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

    def fetch_products(self):
        response = requests.get(f"{self.base_url}/sale/products", headers=self.headers)
        return response.json()

    def create_order(self, order_data):
        response = requests.post(f"{self.base_url}/sale/orders", json=order_data, headers=self.headers)
        return response.json()
