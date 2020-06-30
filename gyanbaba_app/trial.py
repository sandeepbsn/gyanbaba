import requests
import random



response = slack_web_client.conversations_list()
conversations = response["channels"]
pins = []
blocks = []

for channel in conversations:
    link = "https://slack.com/api/pins.list?token=xoxp-1204196757331-1202609854693-1207565989093-4acf2cc88a01f10c5d032af2c65e345f&channel=%s&pretty=1"%(channel['id'])
    r = requests.get(url = link)

    data = r.json()

    pins.append(data)

for pin in pins:
    items = pin['items']
    for item in items:
        if(item.message['blocks']):
            blocks.append(item['message']['blocks'])
        else:
            print("no")

print("blocks",blocks)

"http://7260839bb553.ngrok.io"