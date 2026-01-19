data = [
    {"name": "apple", "category": "fruit"},
    {"name": "carrot", "category": "vegetable"},
    {"name": "banana", "category": "fruit"},
    {"name": "spinach", "category": "vegetable"},
    {"name": "orange", "category": "fruit"},
]


from itertools import groupby

data.sort(key=lambda x: x["category"])

grouped_data={}

for category, item in groupby(data, key=lambda x:x["category"]):
    print(category, list(item))

