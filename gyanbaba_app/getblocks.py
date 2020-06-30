def getReactions(reactions, message_id):
    all_users = ""
    all_users_list = []
    for a in reactions[message_id]:
        all_users_list.append('<@'+a+'>')
    
    for b in all_users_list:
        all_users = all_users + b + ','

    all_users = all_users[:-1]

    return all_users

def quote_block(block_id, data, reactions, message_id):
    all_users = getReactions(reactions, message_id)

    pub_res = [
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
                "text": "*"+data['payload']['text']+"*"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "plain_text",
                    "text": data['payload']['author'],
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
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":bulb: :thinking_face: "+ all_users
            }
        },
        {
            "type": "actions",
            "block_id": str(block_id),
            "elements":[               
                {
                    "type":"button",
                    "text" : {
                        "type":"plain_text",
                        "text": str(data['up_votes']) + ":thumbsup:"
                    },
                    "value":"up_votes",
                    "action_id":"like"
                },
                {
                    "type":"button",
                    "text" : {
                        "type":"plain_text",
                        "text":str(data['down_votes']) + ":thumbsdown:"
                    },
                    "value":"down_votes",
                    "action_id":"dislike"
                }
            ]
        }
    ]

    return pub_res



def joke_block(block_id, data,reactions, message_id):
    all_users = getReactions(reactions, message_id)

    pub_res = [
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": data['payload']['title'],
                    "emoji": True
                },
                "image_url": data['payload']['img_src'],
                "alt_text": "marg"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "plain_text",
                        "text": data['payload']['alt'],
                        "emoji": True
                    }
                ]
            },
            {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":black_joker: "+ all_users
			    }
		    },
            {
                "type": "actions",
                "block_id": str(data['res_id']),
                "elements":[               
                    {
                        "type":"button",
                        "text" : {
                            "type":"plain_text",
                            "text":str(data['up_votes']) + ":thumbsup:"
                        },
                        "value":"up_votes",
                        "action_id":"like"
                    },
                    {
                        "type":"button",
                        "text" : {
                            "type":"plain_text",
                            "text":str(data['down_votes']) + ":thumbsdown:"
                        },
                        "value":"down_votes",
                        "action_id":"dislike"
                    }
                ]
            }
        ]


    return pub_res

def video_block(block_id, data, reactions, message_id):
    all_users = getReactions(reactions, message_id)
    
    pub_res = [
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
                    },			
                ]
            },
            {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":movie_camera: "+ all_users
			    }
		    },
            {
                "type": "actions",
                "block_id": str(data['res_id']),
                "elements":[ 
                                
                    {
                        "type":"button",
                        "text" : {
                            "type":"plain_text",
                            "text":str(data['up_votes']) + ":thumbsup:"
                        },
                        "value":"up_votes",
                        "action_id":"like"
                    },
                    {
                        "type":"button",
                        "text" : {
                            "type":"plain_text",
                            "text":str(data['down_votes']) + ":thumbsdown:"
                        },
                        "value":"down_votes",
                        "action_id":"dislike"
                    }
                ]
            }
        ]

    return pub_res