jsondata = [
        {'id': '1', 'sort': 'kg', 'name': 'meal', 'detail':
            [
                {'subid': 'A', 'name': 'Example', 'values':
                    [
                        {'value': '3', 'time': 320},
                        {'value': '4', 'time': 330},
                        {'value': '5', 'time': 340}
                    ]
                }
            ]
        },
{'id': '2', 'sort': 'lb', 'name': 'meal', 'detail':
            [
                {'subid': 'A', 'name': 'Example', 'values':
                    [
                        {'value': '13', 'time': 1320},
                        {'value': '14', 'time': 2330},
                        {'value': '15', 'time': 3340}
                    ]
                }
            ]
        }
    ]

print(jsondata[0]["detail"][0]["values"][2]["time"])

print(jsondata[0]["detail"][0]["values"])

print(jsondata[0].keys())
print("#"*20)
for each in jsondata:
    print(each)
    print("#" * 20)
for each in jsondata[0]["detail"][0]["values"]:
    print(each)
print("#" * 20)
for each in jsondata[0]["detail"][0]:
    print(each)
print("#" * 20)
for each in jsondata[0]:
    print(each)

print("#"*20,"Second element")
for each in jsondata:
    print(each)
    print("#" * 20)
for each in jsondata[1]["detail"][0]["values"]:
    print(each)
print("#" * 20)
for each in jsondata[1]["detail"][0]:
    print(each)
print("#" * 20)
for each in jsondata[1]:
    print(each)