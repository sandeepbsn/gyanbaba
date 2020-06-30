import requests
import random 
import json  


url = "http://127c11ade942.ngrok.io"


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


def getmeme(text0, text1):
    link = "https://api.imgflip.com/caption_image"

    templates = ['101287', '102156234', '89370399']

    n = random.randint(0,len(templates) - 1)
    
    params = {
        "template_id" : templates[n],
        "username":"gyanbaba20",
        "password":"baba2020",
        "text0":text0,
        "text1":text1,
    }

    res = requests.post(url = link, params = params)

    data = json.loads(res.text)
    print("imaga data os ******", data)
    response = [
		{
			"type": "image",
			"image_url": data['data']['url'],
			"alt_text": "inspiration"
		}
	]

    return response


    

        
    
    



    # [
	# 	{
	# 		"type": "context",
	# 		"elements": [
	# 			{
	# 				"type": "plain_text",
	# 				"text": vid['snippet']['title'],
	# 				"emoji": true
	# 			}
	# 		]
	# 	},
	# 	{
	# 		"type": "context",
	# 		"elements": [
	# 			{
	# 				"type": "image",
	# 				"image_url": "https://cdn.pixabay.com/photo/2016/07/03/18/36/youtube-1495277_960_720.png",
	# 				"alt_text": "cute cat"
	# 			},
    #             {
	# 				"type": "mrkdwn",
	# 				"text": payload['video_url']
	# 			}				
	# 		]
	# 	}
	# ]
    
    



