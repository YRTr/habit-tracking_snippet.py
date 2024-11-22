from user_profile import User
from graph_ import Graph
from pixel import Pixel
from tokenize import token1, token2
import requests

common = 'https://pixe.la/v1/users/'

user_obj = User("riy", token2)
graph_obj = Graph('riy', token2, 'graph2')
pixel_obj = Pixel('riy', token2, 'graph2')

# user_create = user_obj.create_user()
# graph_create = graph_obj.create_graph()
post_pixel = pixel_obj.post_pixel('2')

# print(user_create)
# print(graph_create)
print(post_pixel)

# print(requests.get(f'{common}/@yrtr'))
