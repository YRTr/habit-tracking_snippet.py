import requests
import json


class User:
    def __init__(self, user, req_token):
        self.token = req_token
        self.user_endpoint = "https://pixe.la/v1/users"
        self.username = user
        self.payload = {
            'token': self.token,
            'agreeTermsOFService': 'yes',
            'username': self.username,
            'notMinor': 'yes'
        }
        self.header = {
            'X-USER-TOKEN': self.token
        }

    def create_user(self):
        created = requests.post(url=self.user_endpoint, json=self.payload)
        return created.text

    def update_user(self, new_token):
        params = {
            'newToken': new_token
        }
        updated = requests.put(url=f'{self.user_endpoint}/{self.username}', json=params, headers=self.header)
        print(updated.text)

    def delete_user(self):
        deleted = requests.delete(f'{self.user_endpoint}/{self.username}', headers=self.header)
        print(deleted.text)
