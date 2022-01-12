
query = {'id': 1, 'render_fast': True}
post = {'email': 'j@j.com', 'name': 'Jeff'}
route = {'id': 271, 'title': 'Fast apps'}

# Python 3.10 Pythonic procedural way
merged = query | post | route

print()
print(f'{query=}')
print(f'{post=}')
print(f'{route=}')
print()
print('merged = query | post | route')
print(f'{merged=}')
