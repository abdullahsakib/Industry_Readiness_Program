

# with open ("sakib.jpg","r") as f:
#     data=f.read()


with open ("sakib.jpg","r", encoding="utf-8", errors="ignore") as f:
    data=f.read()


print(type(data))
print(len(data))