from ..services.joke import get_joke
from ..services.quote import get_quote
from ..services.video import get_video
from ..services.resource import load_data,add_vote
from ..services.user import load_user
from ..services.test import get_test
import json
from . import slash
from flask import request


@slash.route('/')
def g_home():
    
    return json.dumps('slash Home')





@slash.route('/joke')
def g_joke():
    # channel_id
    channel_id=request.args['channel_id']
    print('****(((((((******<<<<<<<<JOKE>>>>>>>>>>**********',channel_id)
    joke=get_joke(channel_id)
    # print('in slash route',quote['payload'])

    # return json.dumps({'joke':[dict(row) for row in obj_joke]})
    return json.dumps(joke['payload'][0])
    # print('**********************',joke[0][1])




@slash.route('/quote')
def g_quote():
    channel_id=request.args['channel_id']
    print('****(((((((******<<<<<<<<QUOTE>>>>>>>>>>**********',channel_id)
    
    quote=get_quote(channel_id)
    print('in slash route',quote['payload'])

    # return json.dumps({'joke':[dict(row) for row in obj_joke]})
    return json.dumps(quote['payload'][0])

    # quote=get_quote()
    # print('in slash route',quote['payload'])

    # # return json.dumps({'joke':[dict(row) for row in obj_joke]})
    # return (quote['payload'])
    

@slash.route('/video')
def g_video():
    channel_id=request.args['channel_id']
    print('****(((((((******<<<<<<<<VIDEO>>>>>>>>>>**********',channel_id)
    video=get_video(channel_id)
    # print('in slash route',quote['payload'])

    # return json.dumps({'joke':[dict(row) for row in obj_joke]})
    # return json.dumps(video['payload'])
    print('**********************',video)

    return json.dumps(video['payload'][0])



@slash.route('/addvote/<res_id>',methods=['POST'])
def g_add_vote(res_id):
    user_id=request.json['user_id']
    # user_id=2
    # vote=request.json['vote_value']

    # up_votes,down_votes
    vote_name=request.json['vote_name']

    dd=add_vote({'res_id':res_id,'user_id':user_id,'vote_name':vote_name})

    

    return json.dumps(dd['payload'][0])


@slash.route('/load')
def g_load():
    load_data()
    # load_user()
    return json.dumps('loaded data')


@slash.route('/test')
def g_test():
    # channel_id=request.json['channel_id']
    channel_id="X12KS"
    test=get_test(channel_id)
    # print('in slash route',quote['payload'])

    # return json.dumps({'joke':[dict(row) for row in obj_joke]})
    return json.dumps(test['payload'][0])