query = {'id': 1, 'render_fast': True}
post = {'email': 'j@j.com', 'name': 'Jeff'}
route = {'id': 271, 'title': 'Fast apps'}

# Non-pythonic procedural way
merged = {}
for k in query:
    merged[k] = query[k]
for k in post:
    merged[k] = post[k]
for k in route:
    merged[k] = route[k]


print()
print(f'{query=}')
print(f'{post=}')
print(f'{route=}')
print()
print('Merged via looping')
print(f'{merged=}')
