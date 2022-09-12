# Why? Who knows, anyway here is the single most usless script ever

def load_json_as_variables(fpath:str):
    with open(fpath) as f: c = __import__("json").load(f)
    for k, v in c.items(): globals()[k] = v

load_json_as_variables("test.json")
# test.json ------------------------------------------
# {
#     "fname": "Zackery",
#     "lname": "Smith",
#     "age": 15,
#     "computer": {
#         "OS": "Ubuntu 22.04 LTS x86_64",
#         "host": "Latitude E7450",
#         "kernel": "5.15.0-46-generic",
#         "shell": "zsh 5.8.1",
#         "resolution": "1920x1080",
#         "WM": "i3",
#         "theme": "Breeze [GTK2/3]",
#         "icons": "breeze-dark [GTK2/3]",
#         "terminal": "alacritty",
#         "CPU": "Intel i7-5600U (4) @ 3.200GHz",
#         "GPU": "Intel HD Graphics 5500",
#         "memory": "3450MiB / 15873MiB"
#     }
# }

print(f'{fname} {lname}, {age}')
print(str(computer).replace("{", "{\n    ").replace(",", "\n   ").replace("}", "\n}"))