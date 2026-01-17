
import json

data={
    "name":"sakib",
    "age":"31",
    "skill":"python"
}

with open("file.json","w") as f:
    json.dump(data,f)
