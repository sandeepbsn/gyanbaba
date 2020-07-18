import os
# import logging
from apscheduler.schedulers.background import BackgroundScheduler
# from pytz import timezone
# from tzlocal import get_localzone
from datetime import datetime
from sheduler import modal_pin
from sheduler import modal_scheduler
from flask import Flask
from flask import make_response
from flask import request
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import json
# from onboarding import OnboardingTutorial
from apicalls import *
from getblocks import *
from urllib.parse import urlparse, parse_qs
import requests
from threading import Timer


app = Flask(__name__)
slack_events_adapter = SlackEventAdapter('2d7840bd54b298a8b1a89d4ecdcb0456', "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token='xoxb-1204196757331-1212152498052-9VasQyLSUp061IiwFF4iL0tw')

onboarding_tutorials_sent = {}

user_reacted = {}

schedule_response = {}

pin_channel = {}

@app.route('/',methods=['POST','GET'])
def home22():
    return 'front home'


scheduler = BackgroundScheduler()
scheduler.add_jobstore('sqlalchemy', url='mysql://root:Password_123@localhost/schedule')

scheduler.start()


def schedule_to_print(data):
    #get time to schedule and text to print from the json
    time = data.get('date_time')
    text = data.get('text')
    channels = data.get('channels')
    #convert to datetime
    date_time = datetime.strptime(time, "%d/%m/%Y %H:%M:%S")
    #schedule the method 'printing_something' to run the the given 'date_time' with the args 'text'
    
    job = scheduler.add_job(printing_something, trigger='cron', next_run_time=str(date_time),
                            args=[text, channels], hour=data['hours'], minute=data['minutes'],second=data['seconds'],month='*', coalesce=False, max_instances=1)

    return "job details: %s" % job


def printing_something(text,channels):
    print("printing %s at %s" % (text, datetime.now()))
    print(scheduler.get_jobs())
    
    for channel in channels:
        print("coutn*****", channel)
        params = {
            "token":"xoxb-1204196757331-1212152498052-9VasQyLSUp061IiwFF4iL0tw",
            "channel": channel,
            "text":text,
        }

        requests.post('https://slack.com/api/chat.postMessage', data = params)

    return ""

@app.route('/test', methods = ['POST', 'GET'])
def test_sched():
    data = request.form.to_dict()

    body = {
        "text" : "Fetching content"
    }
    
    requests.post(
        url = data['response_url'], 
        headers = {'Content-Type':'application/json'}, 
        data = json.dumps(body)
    )

    view_res = modal_scheduler()
    slack_web_client.views_open(
        trigger_id = data['trigger_id'],
        view = view_res
    )
    return ""


    # response = slack_web_client.chat_postEphemeral(
    #     channel=data['channel_id'],
    #     blocks=res,
    #     user=data['user_id']
    # )

    # return ""

# @app.route('/slashpin', methods = ['POST', 'GET'])
def slashpin(channel_id, user_id):
    # response = slack_web_client.conversations_list()
    # conversations = response["channels"]
    pins = []
    blocks = []

    # for channel in conversations:
    #     link = "https://slack.com/api/pins.list?token=xoxp-1204196757331-1202609854693-1207565989093-4acf2cc88a01f10c5d032af2c65e345f&channel=%s&pretty=1"%(channel['id'])
    #     r = requests.get(url = link)

    #     data = r.json()

    #     pins.append(data)

    link = "https://slack.com/api/pins.list?token=xoxp-1204196757331-1202609854693-1207565989093-4acf2cc88a01f10c5d032af2c65e345f&channel=%s&pretty=1"%(channel_id)

    r = requests.get(url = link)

    data = r.json()

    pins.append(data)

    print("pins**********", pins)

    pin_items = pins[0]['items']
    for pin in pin_items:
        message = pin['message']['text']
        perma_link = pin['message']['permalink']
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": message,
                }
            },
        )
        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "<"+perma_link+"|View message>"
                }
            }
        )
        # blocks.append((message,perma_link))

    # print("blocks **********",blocks)
    # res_url = request.form.to_dict()

    # body = {
    #     "text" : "Fetching content"
    # }
    
    # requests.post(
    #     url = res_url['response_url'], 
    #     headers = {'Content-Type':'application/json'}, 
    #     data = json.dumps(body)
    # )

    response = slack_web_client.chat_postMessage(
        channel=channel_id,
        blocks=blocks,
        user=user_id
    )

    return ""


@app.route('/pin', methods = ['POST', 'GET'])
def pins():
    data = request.form.to_dict()


    body = {
        "text" : "Fetching content"
    }
    
    requests.post(
        url = data['response_url'], 
        headers = {'Content-Type':'application/json'}, 
        data = json.dumps(body)
    )
    pin_res = modal_pin()
    slack_web_client.views_open(
        trigger_id = data['trigger_id'],
        view = pin_res,
    )

    return ""  

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
        # blocks=res,
        text=res,
        unfurl_links = True,
        unfurl_media = True,
        user=data['user_id']
    )
    else:
        response = slack_web_client.chat_postEphemeral(
        channel=data['channel_id'],
        # blocks=res,
        text=res,
        unfurl_links = True,
        unfurl_media = True,
        user=data['user_id']
    )

    return ""

    


@app.route('/interactions', methods = ['POST'])
def interactions():
    make_response('HTTP 200 OK',200)

    data = request.form.to_dict()
    payload = json.loads(data['payload'])
    #print("paload is ****", payload)

    if payload['type'] == 'block_actions' and payload.get('view')!= None and payload['view']['blocks'][1]['block_id'] == 'pin_channels':
        view_id = payload['view']['id']
        if pin_channel.get(view_id) == None:
            pin_channel[view_id] = {}
            block_id = payload['actions'][0]['block_id']

            value = payload['actions'][0]['selected_channel']

            pin_channel[view_id][block_id] = value
            pin_channel[view_id]['user_id'] = payload['user']['id']

        return ""

    if payload['type'] == 'view_submission' and payload.get('view') != None and payload['view']['blocks'][1]['block_id'] == 'pin_channels':
        print("pin******", pin_channel)
        view_id = payload['view']['id']
        channel_id = pin_channel[view_id]['pin_channels']
        user_id = pin_channel[view_id]['user_id']
        slashpin(channel_id, user_id)

        return ""


    if payload['type'] == 'block_actions' and payload.get('view') != None and payload['view']['blocks'][0]['block_id'] == 'message':
        view_id = payload['view']['id']
        if schedule_response.get(view_id) == None:
            schedule_response[view_id] = {}
            block_id = payload['actions'][0]['block_id']

            if block_id == 'date_sched' or 'date_end':
                cur_date = list(payload['actions'][0]['selected_date'].split('-'))[::-1]
                value = '/'.join(cur_date)
            elif block_id == 'hours' or block_id == 'minutes':
                value = payload['actions'][0]['selected_option']['value']


            schedule_response[view_id][block_id] = value
        else:
            block_id = payload['actions'][0]['block_id']

            if block_id == 'date_sched' or block_id == 'date_end':
                cur_date = list(payload['actions'][0]['selected_date'].split('-'))[::-1]
                value = '/'.join(cur_date)
            elif block_id == 'hours' or block_id == 'minutes':
                value = payload['actions'][0]['selected_option']['value']
            # elif block_id == 'channels':
            #     value = payload['actions'][0]['selected_channel']
            elif block_id == 'users':
                value = payload['actions'][0]['selected_user']

            schedule_response[view_id][block_id] = value

        return ""

    if payload['type'] == 'view_submission' and payload.get('view') != None and payload['view']['blocks'][0]['block_id'] == 'message':
        text = payload['view']['state']['values']['message']['text']['value']
        channels = payload['view']['state']['values']['channels']['name']['selected_channels']
        
        view_id = payload['view']['id']
        # if schedule_response.get(view_id) == None:
        #     schedule_response[view_id] = {}

        if view_id not in schedule_response:
            return {"response_action":"clear"}            

        if schedule_response[view_id].get('hours') == None or schedule_response[view_id].get('minutes') == None:
            return {"response_action":"clear"}            

        if schedule_response[view_id].get('date_sched') == None:
            schedule_response[view_id]['date_sched'] = datetime.now().date().strftime('%d/%m/%Y')

        if schedule_response[view_id].get('date_end') == None:
            schedule_response[view_id]['date_end'] = datetime.now().date().strftime('%d/%m/%Y')


        schedule_response[view_id]['seconds'] = '00'
        schedule_response[view_id]['text'] = text
        schedule_response[view_id]['channels'] = channels

        schedule_response[view_id]['time'] = schedule_response[view_id]['hours'] + ":" + schedule_response[view_id]['minutes'] + ":" + schedule_response[view_id]['seconds'] 

        schedule_response[view_id]['date_time'] = schedule_response[view_id]['date_sched'] + " " + schedule_response[view_id]['time']

        schedule_to_print(schedule_response[view_id])
        
        print("response*************", schedule_response)
        return {"response_action":"clear"}

    if payload['type'] == 'view_submission' and payload.get('view') != None and payload['view']['blocks'][0]['block_id'] == '0':
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
        return ""

    else:
        if payload['container']['message_ts'] in user_reacted:
            if payload['user']['id'] not in user_reacted[payload['container']['message_ts']]:
                user_reacted[payload['container']['message_ts']].append(payload['user']['id'])
        else: 
            user_reacted[payload['container']['message_ts']] = []
            user_reacted[payload['container']['message_ts']].append(payload['user']['id'])

        #print("user reacted is ********", user_reacted)

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

        url = "http://gyanbaba-api.abhisheksaklani.co/slash/addvote/"+payload['actions'][0]['block_id']

        res = requests.post(url, json = params)

        data = json.loads(res.text)

        #print("data response is ******", data)

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




        

    









