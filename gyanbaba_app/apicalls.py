import requests
import random 
import json  

def load_meme():
    url = "http://gyanbaba-api.abhisheksaklani.co"

    mem = requests.get(url+"/slash/getallmeme")

    all_memes = mem.json()

    meme_details = {}

    for meme in all_memes:
        meme_details[meme['id']] = [meme['name'], meme['box_count'], meme['url']]

    return meme_details

#function to fetch jokes from slash command(/joke)
def getjoke(channel_id, command_text):
    link = url+"/slash/joke"

    params = {
        "channel_id" : channel_id
    }

    r = requests.get(url = link, params=params, timeout = 5)

    data = r.json()

    if(data['flag']):
        payload = data['payload']
        response = [
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": payload['title'],
                    "emoji": True
                },
                "image_url": payload['img_src'],
                "alt_text": "marg"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "plain_text",
                        "text": payload['alt'],
                        "emoji": True
                    }
                ]
            },
            {
                "type": "actions",
                "block_id": str(data['res_id']),
                "elements":[               
                    {
                        "type":"button",
                        "text" : {
                            "type":"plain_text",
                            "text":str(data['up_votes']) + " :thumbsup:" if (command_text) else ":thumbsup:"
                        },
                        "value":"up_votes",
                        "action_id":"like"
                    },
                    {
                        "type":"button",
                        "text" : {
                            "type":"plain_text",
                            "text":str(data['down_votes']) + " :thumbsdown:" if command_text else ":thumbsdown:"
                        },
                        "value":"down_votes",
                        "action_id":"dislike"
                    }
                ]
            }
        ]

        return response
    else:
        response = [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSICPv2MB4cg-5-iBDaIUchCuFZrUoJSSAfXw&usqp=CAU",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "mrkdwn",
                        "text": data['payload']['text']				
                    }
                ]
            }
	    ]

        return response


    
    



#function to fetch quotes from slash command(/quote)
def getquote(channel_id, command_text):
    link = url+"/slash/quote"

    params = {
        "channel_id" : channel_id
    }

    r = requests.get(url = link, params = params)

    data = r.json()

    if(data['flag']):
        payload = data['payload']
        response = [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRld4Bm0nOgnHNGovthoFmv0nSQ3PGwcuc3lQ&usqp=CAU",
                        "alt_text": "images"
                    },
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*"+payload['text']+"*"
                }
		    },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "plain_text",
                        "text": payload['author'],
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQX1tp-rGeQ70l7ZPCQAIxkbqeVdvzMlvsBfQ&usqp=CAU",
                        "alt_text": "images"
                    },
                ]
            },
            {
                "type": "actions",
                "block_id": str(data['res_id']),
                "elements":[               
                    {
                        "type":"button",
                        "text" : {
                            "type":"plain_text",
                            "text": str(data['up_votes']) + " :thumbsup:" if (command_text) else ":thumbsup:"
                        },
                        "value":"up_votes",
                        "action_id":"like"
                    },
                    {
                        "type":"button",
                        "text" : {
                            "type":"plain_text",
                            "text":str(data['down_votes']) + " :thumbsdown:" if command_text else ":thumbsdown:"
                        },
                        "value":"down_votes",
                        "action_id":"dislike"
                    }
                ]
            }
            
        ]

        return response
    else:
        response = [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSICPv2MB4cg-5-iBDaIUchCuFZrUoJSSAfXw&usqp=CAU",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "mrkdwn",
                        "text": data['payload']['text']				
                    }
                ]
            }
	    ]

        return response
        

#function to fetch videos from slash command(/video)
def getvideo(channel_id, command_text):
    link = url+"/slash/video"

    params = {
        "channel_id" : channel_id
    }

    r = requests.get(url = link, params = params)

    data = r.json()

    if(data['flag']):
        payload = data['payload']
        response = [
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "plain_text",
                            "text": data['payload']['title'],
                            "emoji": True
                        }
                    ]
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "image",
                            "image_url": "https://cdn.pixabay.com/photo/2016/07/03/18/36/youtube-1495277_960_720.png",
                            "alt_text": "cute cat"
                        },
                        {
                            "type": "mrkdwn",
                            "text": data['payload']['video_url']
                        }				
                    ]
                },
                {
                    "type": "actions",
                    "block_id": str(data['res_id']),
                    "elements":[ 
                                    
                        {
                            "type":"button",
                            "text" : {
                                "type":"plain_text",
                                "text":str(data['up_votes']) + " :thumbsup:" if (command_text) else ":thumbsup:"
                            },
                            "value":"up_votes",
                            "action_id":"like"
                        },
                        {
                            "type":"button",
                            "text" : {
                                "type":"plain_text",
                                "text":str(data['down_votes']) + " :thumbsdown:" if command_text else ":thumbsdown:"
                            },
                            "value":"down_votes",
                            "action_id":"dislike"
                        }
                    ]
                }
            ]
        return response
    else:
        response = [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSICPv2MB4cg-5-iBDaIUchCuFZrUoJSSAfXw&usqp=CAU",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "mrkdwn",
                        "text": data['payload']['text']				
                    }
                ]
            }
        ]
        
        return response

def gethelp():
    response = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Ping me whenever you are bored using these commands -*GyanBaba*"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*/enlightenme publicly*\n\n This would post a quote on the channel"
			},
			"accessory": {
				"type": "image",
				"image_url": "https://i.imgur.com/IjliNvd.png",
				"alt_text": "alt text for image"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*/enlightenme *\n\n This would post a quote only visible to you. "
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*/boostme publicly*\n\n This would post a video on the channel"
			},
			"accessory": {
				"type": "image",
				"image_url": "https://i.imgur.com/0DlERY2.png",
				"alt_text": "alt text for image"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*/boostme *\n\n This would post a video only visible to you"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*/tellmeajoke publicly*\n\n This would post a joke on the channel"
			},
			"accessory": {
				"type": "image",
				"image_url": "https://i.imgur.com/pkVvaaM.png",
				"alt_text": "alt text for image"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*/tellmeajoke*\n\n This would post a joke only visible to you"
			}
		},
		{
			"type": "divider"
		}
	]

    return response


def getmeme():
    option_block = []
    meme_details = load_meme()
    for keys in meme_details:
        option = {
            "text": {
                "type": "plain_text",
                "text": meme_details[keys][0],
                "emoji": True
            },
            "value": keys
        }
        option_block.append(option)


    response = [
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick an item from the dropdown list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": option_block
			}
		}
	]
    

    return response


def fetchmeme(meme_id, user_id, channel_id):

    # templates = {
    #     "112126428": ['distracted_boyfriend', '3', 'https://i.kym-cdn.com/photos/images/newsfeed/001/287/547/e06.jpg'],
    #     "87743020": ['two_buttons', '2', 'https://i.imgflip.com/2aux46.jpg'],
    #     "93895088":['expanding brain', '4', 'https://66.media.tumblr.com/668f8fa044b09642396ee8be9846b449/tumblr_olspqaVPMy1u9ru6ro1_1280.png']
    # }
    meme_details = load_meme()

    text_required = int(meme_details[meme_id][1])
    img_url = meme_details[meme_id][2]

    array_one = []
    for i in range(text_required):
        array_one.append(
            {
                "type": "input",
                "block_id":str(i),
                "element": {
                    "type": "plain_text_input",
                    "action_id":str(i)
                },
                "label": {
                    "type": "plain_text",
                    "text": "Text "+str(i+1),
                    "emoji": True
                }
            },
        )

    array_one.append(
        {
            "type": "image",
            "image_url": img_url,
            "alt_text": meme_id + " " + user_id + " " + channel_id
        }
    )
        

    response = {
        "type": "modal",
        "title": {
            "type": "plain_text",
            "text": "My App",
            "emoji": True
        },
        "submit": {
            "type": "plain_text",
            "text": "Submit",
            "emoji": True
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True
        },
        "blocks": array_one
    }

    return response


def req_meme(text_array, ids):
    link = "https://api.imgflip.com/caption_image"

    id_array = ids.split()

    if len(text_array) == 1:
        params = {
            "template_id" : id_array[0],
            "username":"gyanbaba20",
            "password":"baba2020",
            "boxes[0][text]": text_array[0],
        }
    elif len(text_array) == 2:
        params = {
            "template_id" : id_array[0],
            "username":"gyanbaba20",
            "password":"baba2020",
            "boxes[0][text]": text_array[0],
            "boxes[1][text]": text_array[1],
        }
    elif len(text_array) == 3:
        params = {
            "template_id" : id_array[0],
            "username":"gyanbaba20",
            "password":"baba2020",
            "boxes[0][text]": text_array[0],
            "boxes[1][text]": text_array[1],
            "boxes[2][text]": text_array[2],
        }
    elif len(text_array) == 4:
        params = {
            "template_id" : id_array[0],
            "username":"gyanbaba20",
            "password":"baba2020",
            "boxes[0][text]": text_array[0],
            "boxes[1][text]": text_array[1],
            "boxes[2][text]": text_array[2],
            "boxes[3][text]": text_array[3],
        }
    elif len(text_array) == 5:
        params = {
            "template_id" : id_array[0],
            "username":"gyanbaba20",
            "password":"baba2020",
            "boxes[0][text]": text_array[0],
            "boxes[1][text]": text_array[1],
            "boxes[2][text]": text_array[2],
            "boxes[3][text]": text_array[3],
            "boxes[4][text]": text_array[4],
        }
    

    res = requests.get(url = link, params = params)

    data = json.loads(res.text)
    #print("imaga data os ******", data)
    response = [
		{
			"type": "image",
			"image_url": data['data']['url'],
			"alt_text": "inspiration"
		}
	]

    return {
        "response": response,
        "user_id": id_array[1],
        "channel_id": id_array[2]
    }
