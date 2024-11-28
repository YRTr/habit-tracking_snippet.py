import requests


class Graph:
    def __init__(self, user, req_token, graphid):
        self.username = user
        self.end_point = f'https://pixe.la/v1/users'
        self.payload = {
            'id': graphid,
            'name': 'progress',
            'unit': 'hours',
            'type': 'int',
            'color': 'ajisai',
        }
        self.header = {
            'X-USER-TOKEN': req_token
        }

    def create_graph(self):
        response = requests.post(url=f'{self.end_point}/{self.username}/graphs', json=self.payload, headers=self.header)
        return response.text

    def helper(self):
        print("Get all predefined pixelation graph definitions.")
        g_def = requests.get(url=f'{self.end_point}/{self.username}/graphs', headers=self.header)
        return g_def.json()

    def graph_define(self):
        print("Get a predefined pixelation graph definition")
        define = requests.get(url=f'{self.end_point}/{self.username}/graphs/{self.payload['id']}/graph-def', headers=self.header)
        return define.json()

    def graph_svg(self):
        print("Based on the registered information, express the graph in SVG format diagram")
        svg = requests.get(url=f'{self.end_point}/{self.username}/graphs/{self.payload['id']}')
        return svg

    def update_graph(self):
        print("Update predefined pixelation graph definitions. The items that can be updated are limited as compared with the pixelation graph definition creation.")
        optional = {
            'name': self.payload['name'],
            'unit': self.payload['unit'],
            'color': self.payload['color']
        }
        updated = requests.put(url=f'{self.end_point}/{self.username}/graphs/{self.payload['id']}', headers=self.header)
        return updated.text

    def delete_graph(self):
        print("Delete predefined pixelation graph definition")
        deleted = requests.delete(url=f'{self.end_point}/{self.username}/graphs/{self.payload['id']}', headers=self.header)
        return deleted.text

    def view_graph(self):
        print("Displays the details of the graph in html format")
        optional = {
            'mode': 'simple'
        }
        return requests.get(url=f'{self.end_point}/{self.username}/graphs/{self.payload['id']}.html')


