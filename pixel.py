import requests
from datetime import datetime


class Pixel:
    def __init__(self, user, req_token, graphid):
        self.today = datetime.now().strftime("%Y%m%d")
        self.username = user
        self.graphID = graphid
        self.end_point = f'https://pixe.la/v1/users'
        self.header = {
            'X-USER-TOKEN': req_token
        }

    def post_pixel(self, count):
        print("It records the quantity of the specified date as a 'Pixel'")
        params = {
            'date': self.today,
            'quantity': count
        }
        posted = requests.post(url=f'{self.end_point}/{self.username}/graphs/{self.graphID}', json=params, headers=self.header)
        return posted.text

    def quant_pixel(self, date_str):
        print("Get registered quantity as 'Pixel'")
        quantity = requests.get(url=f'{self.end_point}/{self.username}/graphs/{self.graphID}/{self.today}/{date_str}', headers=self.header)
        return quantity.text

    def update_pixel(self, date_str):
        print("Update the quantity already registered as a 'Pixel'. If target 'Pixel' not exist, create a new 'Pixel' and set quantity")
        updated = requests.put(url=f'{self.end_point}/{self.username}/graphs/{self.graphID}/{self.today}/{date_str}', headers=self.header)
        return updated.text

    def delete_pixel(self, date_str):
        print("Delte the registered 'Pixel'")
        deleted = requests.delete(url=f'{self.end_point}/{self.username}/graphs/{self.graphID}/{self.today}/{date_str}', headers=self.header)
        return deleted.text