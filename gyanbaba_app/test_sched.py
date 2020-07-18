from flask import Flask
from flask import request
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import requests

schedule_app = Flask(__name__)

scheduler = BackgroundScheduler()

scheduler.start()

@schedule_app.route('/schedulePrint', methods=['POST'])
def schedule_to_print():
    data = request.get_json()
    #get time to schedule and text to print from the json
    time = data.get('time')
    text = data.get('text')
    #convert to datetime
    date_time = datetime.strptime(time, "%d/%m/%Y %H:%M:%S")
    #schedule the method 'printing_something' to run the the given 'date_time' with the args 'text'
    job = scheduler.add_job(printing_something, trigger='date', next_run_time=str(date_time),
                            args=[text])
    return "job details: %s" % job


def printing_something(text):
    print("printing %s at %s" % (text, datetime.now()))
    print(scheduler.get_jobs())
    params = {
        "token":"xoxb-1204196757331-1212152498052-9VasQyLSUp061IiwFF4iL0tw",
        "channel": "C015ZV2BXQS",
        "text":"testing one",
    }

    requests.post('https://slack.com/api/chat.postMessage', data = params)

