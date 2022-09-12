from requests import post

USERNAME = "Zackery's webhook"
WEBHOOK = "WEBHOOK URL"

# Here is an example of an embed. Using all features possible.
# Feel free to remove or edit things.
EMBED = {
    "type": "rich",
    "color": 7419530, 
    "title": "Embed sent only using the requests module :O",
    "description": "Only the best description ever",
    "fields": [
        {
            "name":"Field1",
            "value":"Here is some text in the field",
            "inline":False
        }
    ],
    "image": {
        "url": "https://avatars.githubusercontent.com/u/72983221?v=4"
        #"proxy_url": "Add a proxy URL if you'd like",
        #"height": 10,
        #"width": 10
    },
    "thumbnail": {
        "url": "https://avatars.githubusercontent.com/u/72983221?v=4"
        #"proxy_url": "Add a proxy URL if you'd like"
        #"height": 10,
        #"width": 10
    },
    "author": {
        "name": "Zackery",
        "url": "https://github.com/ZackeryRSmith",
        "icon_url": "https://avatars.githubusercontent.com/u/72983221?v=4"
        #"proxy_icon_url": "Add a proxy URL if you'd like"
    },
    "timestamp": "2007-08-23T04:00:00.00Z",  # YYYY-MM-DDTHH:MM:SS
    "footer": {
        "text": "Feet!? Nasty",
        "icon_url": "https://avatars.githubusercontent.com/u/72983221?v=4"
        #"proxy_icon_url": "Add a proxy URL if you'd like"
    }
}

post(WEBHOOK,json={
        "username": USERNAME,
        "content": "Hey! Here is a webhook example using the requests module!",
        # You may specify multible embeds
        "embeds":[EMBED]
    }
)