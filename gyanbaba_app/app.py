import os
import logging
from flask import Flask
from flask import request
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import json
from onboarding import OnboardingTutorial
from apicalls import *
from getblocks import *
from urllib.parse import urlparse, parse_qs
import requests
from threading import Timer


app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

onboarding_tutorials_sent = {}

user_reacted = {}


@app.route('/quote', methods= ['POST','GET'])
def slash_quote():
    data = request.form.to_dict()

    body = {
        "text" : "Fetching content"
    }
    
    requests.post(
        url = data['response_url'], 
        headers = {'Content-Type':'application/json'}, 
        data = json.dumps(body)
    )

    res = getquote(data['channel_id'], data['text'])

    if(data['text'] == 'publicly'):
        response = slack_web_client.chat_postMessage(
        channel=data['channel_id'],
        blocks=res,
        user=data['user_id']
    )
    else:
        response = slack_web_client.chat_postEphemeral(
        channel=data['channel_id'],
        blocks=res,
        user=data['user_id']
    )    


    return ""



@app.route('/joke', methods= ['POST','GET'])
def slash_joke():
    data = request.form.to_dict()

    body = {
        "text" : "Fetching content"
    }
    
    requests.post(
        url = data['response_url'], 
        headers = {'Content-Type':'application/json'}, 
        data = json.dumps(body)
    )

    res = getjoke(data['channel_id'], data['text'])

    

    if(data['text'] == 'publicly'):
        response = slack_web_client.chat_postMessage(
        channel=data['channel_id'],
        blocks=res,
        user=data['user_id']
    )
    else:
        response = slack_web_client.chat_postEphemeral(
        channel=data['channel_id'],
        blocks=res,
        user=data['user_id']
    )

    return ""

@app.route('/video', methods= ['POST','GET'])
def slash_video():
    data = request.form.to_dict()

    body = {
        "text" : "Fetching content"
    }
    
    requests.post(
        url = data['response_url'], 
        headers = {'Content-Type':'application/json'}, 
        data = json.dumps(body)
    )

    res = getvideo(data['channel_id'], data['text'])


    if(data['text'] == 'publicly'):
        response = slack_web_client.chat_postMessage(
        channel=data['channel_id'],
        # token = 'xoxp-1204196757331-1202609854693-1207565989093-4acf2cc88a01f10c5d032af2c65e345f',
        as_user = True,
        blocks=res,
        unfurl_links = True,
        unfurl_media = True,
        user=data['user_id']
    )
    else:
        response = slack_web_client.chat_postEphemeral(
        channel=data['channel_id'],
        blocks=res,
        unfurl_links = True,
        unfurl_media = True,
        user=data['user_id']
    )

    return ""

    


@app.route('/interactions', methods = ['POST'])
def interactions():

    data = request.form.to_dict()
    payload = json.loads(data['payload'])
    print("paload is ****", payload)

    if payload['type'] == 'view_submission':
        text_req = len(payload['view']['blocks']) - 1
        texts = payload['view']['state']['values']
        
        text_arr = []
        for i in range(text_req):
            text_arr.append(texts[str(i)][str(i)]['value'])

        response = req_meme(text_arr, payload['view']['blocks'][-1]['alt_text'])

        msg = slack_web_client.chat_postMessage(
            channel=response['channel_id'],
            blocks=response['response'],
            user=response['user_id']
        )
        return {"response_action":"clear"}

    if payload['actions'][0]['type'] == 'static_select':
        user_id = payload['user']['id']
        channel_id = payload['container']['channel_id']
        meme_id = payload['actions'][0]['selected_option']['value']
        response = fetchmeme(meme_id, user_id, channel_id)
        slack_web_client.views_open(
            trigger_id = payload['trigger_id'],
            view = response,
        )

        

        # slack_web_client.chat_delete(
        #     channel = payload['channel']['id'],
        #     ts = payload['container']['message_ts'],
        #     as_user = True
        # )
            
        return ""

    else:
        if payload['container']['message_ts'] in user_reacted:
            if payload['user']['id'] not in user_reacted[payload['container']['message_ts']]:
                user_reacted[payload['container']['message_ts']].append(payload['user']['id'])
        else: 
            user_reacted[payload['container']['message_ts']] = []
            user_reacted[payload['container']['message_ts']].append(payload['user']['id'])

        print("user reacted is ********", user_reacted)

        requests.post(
            url = payload['response_url'], 
            headers = {'Content-Type':'application/json'}, 
            json = {"response_type" : "in_channel" }
        )
        
        params = {
            "user_id": payload['user']['id'],
            "vote_name" : payload['actions'][0]['value'],
            "channel_id" : payload['container']['channel_id']
        }

        url = "http://127c11ade942.ngrok.io/slash/addvote/"+payload['actions'][0]['block_id']

        res = requests.post(url, json = params)

        data = json.loads(res.text)

        print("data response is ******", data)

        if(data['category_name'] == 'quote'):
            pub_res = quote_block(payload['actions'][0]['block_id'], data, user_reacted, payload['container']['message_ts'])
        elif(data['category_name'] == 'joke'):
            pub_res = joke_block(payload['actions'][0]['block_id'], data, user_reacted, payload['container']['message_ts'])
        elif(data['category_name'] == 'video'):
            pub_res = video_block(payload['actions'][0]['block_id'], data, user_reacted, payload['container']['message_ts'])

        

        priv_res = [
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": ":tada: :confetti_ball:  Thanks for your response  :tada: :confetti_ball:",
                    "emoji": True
                }
            }
        ]

        if(payload['container']['is_ephemeral'] == True and data['footprint'] == True):
            update_mgs = slack_web_client.chat_postEphemeral(
            channel = payload['channel']['id'],
            user = payload['user']['id'],
            blocks=priv_res
        )
        elif(payload['container']['is_ephemeral'] == False):
            update_mgs = slack_web_client.chat_update(
            channel = payload['channel']['id'],
            ts = payload['container']['message_ts'],
            as_user = 'true',
            blocks=pub_res
        )

        return ""

@app.route('/help', methods= ['POST','GET'])
def slash_help():
    data = request.form.to_dict()

    body = {
        "text" : "Fetching content"
    }
    
    requests.post(
        url = data['response_url'], 
        headers = {'Content-Type':'application/json'}, 
        data = json.dumps(body)
    )

    res = gethelp()


    msg = slack_web_client.chat_postEphemeral(
        channel = data['channel_id'],
        user = data['user_id'],
        blocks=res
    )


    return ""


@app.route('/meme', methods= ['POST','GET'])
def slash_meme():
    data = request.form.to_dict()

    body = {
        "text" : "Fetching content"
    }
    
    requests.post(
        url = data['response_url'], 
        headers = {'Content-Type':'application/json'}, 
        data = json.dumps(body)
    )

    res = getmeme()


    if(data['text'] == 'publicly'):
        response = slack_web_client.chat_postMessage(
        channel=data['channel_id'],
        blocks=res,
        user=data['user_id']
    )
    else:
        response = slack_web_client.chat_postEphemeral(
        channel=data['channel_id'],
        blocks=res,
        user=data['user_id']
    )

    return ""


    




    










    # res = [
	# 	{
	# 		"type": "section",
	# 		"text": {
	# 			"type": "plain_text",
	# 			"text": "thanks for your resonse" if(x.text == 'true') else "",
	# 			"emoji": True
	# 		}
	# 	}
	# ]

    # response = slack_web_client.chat_postEphemeral(
    #         channel='C01664YDXD2',
    #         blocks=res,
    #         user=payload['user']['id']
    #     )

    # update_mgs = slack_web_client.chat_update(
    #     channel = 'C01664YDXD2',
    #     ts = '1593286929.037900',
    #     as_user = 'true',
    #     text="updated message"

    # )

#     return {
# 	"blocks": [
# 		{
# 			"type": "section",
# 			"text": {
# 				"type": "plain_text",
# 				"text": "Hello user.",
# 				"emoji": True
# 			}
# 		}
# 	]
# }

















# def start_onboarding(user_id: str, channel: str):
#     # Create a new onboarding tutorial.
#     onboarding_tutorial = OnboardingTutorial(channel)

#     # Get the onboarding message payload
#     message = onboarding_tutorial.get_message_payload()

#     # Post the onboarding message in Slack
#     response = slack_web_client.chat_postMessage(**message)

#     # Capture the timestamp of the message we've just posted so
#     # we can use it to update the message after a user
#     # has completed an onboarding task.
#     onboarding_tutorial.timestamp = response["ts"]

#     # Store the message sent in onboarding_tutorials_sent
#     if channel not in onboarding_tutorials_sent:
#         onboarding_tutorials_sent[channel] = {}
#     onboarding_tutorials_sent[channel][user_id] = onboarding_tutorial


# # @slack_events_adapter.on("team_join")
# # def onboarding_message(payload):
# #     """Create and send an onboarding welcome message to new users. Save the
# #     time stamp of this message so we can update this message in the future.
# #     """
# #     event = payload.get("event", {})

# #     # Get the id of the Slack user associated with the incoming event
# #     user_id = event.get("user", {}).get("id")

# #     # Open a DM with the new user.
# #     response = slack_web_client.im_open(user_id)
# #     channel = response["channel"]["id"]

# #     # Post the onboarding message.
# #     start_onboarding(user_id, channel)


# # # ============= Reaction Added Events ============= #
# # # When a users adds an emoji reaction to the onboarding message,
# # # the type of the event will be 'reaction_added'.
# # # Here we'll link the update_emoji callback to the 'reaction_added' event.
# # @slack_events_adapter.on("reaction_added")
# # def update_emoji(payload):
# #     """Update the onboarding welcome message after receiving a "reaction_added"
# #     event from Slack. Update timestamp for welcome message as well.
# #     """
# #     event = payload.get("event", {})

# #     channel_id = event.get("item", {}).get("channel")
# #     user_id = event.get("user")

# #     if channel_id not in onboarding_tutorials_sent:
# #         return

# #     # Get the original tutorial sent.
# #     onboarding_tutorial = onboarding_tutorials_sent[channel_id][user_id]

# #     # Mark the reaction task as completed.
# #     onboarding_tutorial.reaction_task_completed = True

# #     # Get the new message payload
# #     message = onboarding_tutorial.get_message_payload()

# #     # Post the updated message in Slack
# #     updated_message = slack_web_client.chat_update(**message)

# #     # Update the timestamp saved on the onboarding tutorial object
# #     onboarding_tutorial.timestamp = updated_message["ts"]


# # # =============== Pin Added Events ================ #
# # # When a users pins a message the type of the event will be 'pin_added'.
# # # Here we'll link the update_pin callback to the 'reaction_added' event.
# # @slack_events_adapter.on("pin_added")
# # def update_pin(payload):
# #     """Update the onboarding welcome message after receiving a "pin_added"
# #     event from Slack. Update timestamp for welcome message as well.
# #     """
# #     event = payload.get("event", {})

# #     channel_id = event.get("channel_id")
# #     user_id = event.get("user")

# #     # Get the original tutorial sent.
# #     onboarding_tutorial = onboarding_tutorials_sent[channel_id][user_id]

# #     # Mark the pin task as completed.
# #     onboarding_tutorial.pin_task_completed = True

# #     # Get the new message payload
# #     message = onboarding_tutorial.get_message_payload()

# #     # Post the updated message in Slack
# #     updated_message = slack_web_client.chat_update(**message)

# #     # Update the timestamp saved on the onboarding tutorial object
# #     onboarding_tutorial.timestamp = updated_message["ts"]


# # # ============== Message Events ============= #
# # # When a user sends a DM, the event type will be 'message'.
# # # Here we'll link the message callback to the 'message' event.
# # @slack_events_adapter.on("message")
# # def message(payload):
# #     """Display the onboarding welcome message after receiving a message
# #     that contains "start".
# #     """
# #     event = payload.get("event", {})

# #     channel_id = event.get("channel")
# #     user_id = event.get("user")
# #     text = event.get("text")


# #     if text and text.lower() == "start":
# #         return start_onboarding(user_id, channel_id)
    
# #     elif text and text.lower() == "joke":
# #         res = getjoke()
# #         response = slack_web_client.chat_postMessage(
# #             channel=payload['event']['channel'],
# #             blocks=res
# #         )
# #         return

# #     elif text and text.lower() == "quote":
# #         res = getquote()
# #         response = slack_web_client.chat_postMessage(
# #             channel=payload['event']['channel'],
# #             blocks=res
# #         )
# #         return

# #     elif "video" in text and text.lower():
# #         video_res = getvideo()

        # response = slack_web_client.chat_postMessage(
        #     channel=payload['event']['channel'],
        #     text=video_res['video_url'],
        #     blocks=video_res['response']
        # )
        # return


# # @slack_events_adapter.on("channel_rename")
# # def getcommand(payload):
# #     val = "nice name"
# #     response = slack_web_client.chat_postMessage(
# #             channel=payload['event']['channel']['id'],
# #             text=val
# #         )

# #     return




        

    









