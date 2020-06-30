from ..models import db
from ..models.ResourceModel import Resource 
from ..models.CategoryModel import Category
from ..models.FootprintModel import Footprint
import requests
import asyncio


def load_quote_from_api():
    link = "https://type.fit/api/quotes"

    r = requests.get(url = link)

    data = r.json()
    # print("*****||||||||*******|||||||****",data)
    return data

def load_joke_from_api(num):
    link = "https://xkcd.com/"+str(num)+"/info.0.json"

    r = requests.get(url = link)

    data = r.json()

    return data


def load_video_from_api(keyword):
    link = "https://www.googleapis.com/youtube/v3/search?part=snippet&eventType=none&maxResults=5&q=motivate%7Cmotivation%7Cpeace%7Cgym%7Cmeditate%7Cyoga&type=videos&key=AIzaSyCeqh23QCsljI-FccBXAmEEpMgPuFbMo2E"
    r = requests.get(url = link)
    data = r.json()

    data = data['items']

    # video_url = "https://youtube.com/watch?v="+cur

    return data
    


def load_cat():
    cat1=Category(title='joke')
    db.session.add(cat1)
    cat2=Category(title='quote')
    db.session.add(cat2)
    cat3=Category(title='video')
    db.session.add(cat3)

    db.session.commit()

def load_data():
    load_cat()
    quote_payload=load_quote_from_api()
    res=db.session.execute('select id from category where title="quote"')
    for a in res:
        cat_id=a[0]
        break
    
    for i in range(0,5):
        quote=Resource(cat_id=cat_id,payload=quote_payload[i])
        db.session.add(quote)
    
    db.session.commit()


    res=db.session.execute('select id from category where title="joke"')
    for a in res:
        cat_id=a[0]
        break
    print('***************',cat_id)

    # for i in range(1,10):
    for j in range(10,15):
        payload=load_joke_from_api(j)
        joke_payload={"alt":payload['alt'],"img_src":payload['img'],"title":payload['safe_title']}
        joke=Resource(cat_id=cat_id,payload=joke_payload)
        db.session.add(joke)

    db.session.commit()


    
    video_payload=load_video_from_api('')
    res=db.session.execute('select id from category where title="video"')
    for a in res:
        cat_id=a[0]
        break
    
    for i in range(0,len(video_payload)):
        if video_payload[i]['id']['kind']=="youtube#video":
            payload={"title":video_payload[i]['snippet']['title'],"description":video_payload[i]['snippet']['description'],"video_url":"https://youtube.com/watch?v="+video_payload[i]['id']["videoId"]}
            vid=Resource(cat_id=cat_id,payload=payload)
            db.session.add(vid)
    
    db.session.commit()
    
    return {'success'}


def add_vote(payload):
    res_id=payload['res_id']
    user_id=payload['user_id']
    vote_name=payload['vote_name']

    # dat={"user_id":user_id,"res_id":id}
    # res12=db.session.execute('select * from footprint where id=:user_id AND resource_id=:res_id',data)
    res12=Footprint.query.filter(Footprint.resource_id==res_id,Footprint.user_id==user_id).all()
    flag=0
    foot_flag=False
    up_c=0
    d_c=0
    if res12:
        for a in res12:
            flag=1
            up_c=a.up_votes
            d_c=a.down_votes
            break

    if(flag==0):
        if vote_name=='up_votes':
            foot_flag=True
            foot=Footprint(resource_id=res_id,user_id=user_id,up_votes=1)
            db.session.add(foot)
            query='UPDATE resource SET up_votes=up_votes+1 WHERE id="%s"'%res_id
            db.session.execute(query)
            db.session.commit()
        else:
            foot_flag=True
            foot=Footprint(resource_id=res_id,user_id=user_id,down_votes=1)
            db.session.add(foot)
            query='UPDATE resource SET down_votes=down_votes+1 WHERE id="%s"'%res_id
            db.session.execute(query)
            db.session.commit()
    
    
    if flag==1:
        if up_c==1 and vote_name=="down_votes":
            foot_flag=True
            u_foot=Footprint.query.filter(Footprint.resource_id==res_id,Footprint.user_id==user_id).first()
            u_foot.up_votes=0
            u_foot.down_votes=1
            u_res='UPDATE resource SET down_votes=down_votes+1,up_votes=up_votes-1 WHERE id="%s"'%res_id
            db.session.execute(u_res)
            db.session.commit()
        elif d_c==1 and vote_name=="up_votes":
            foot_flag=True
            d_foot=Footprint.query.filter(Footprint.resource_id==res_id,Footprint.user_id==user_id).first()
            d_foot.up_votes=1
            d_foot.down_votes=0
            d_res='UPDATE resource SET down_votes=down_votes-1,up_votes=up_votes+1 WHERE id="%s"'%res_id
            db.session.execute(d_res)
            db.session.commit()

    





    

    res2=Resource.query.filter(Resource.id.like(res_id)).all()
    data2=[]
    
    for d in res2:
        print("from adddd vote",d.payload)
        temp_dict={}
        res_id=d.id
        temp_dict['res_id']=d.id
        # temp_dict['flag']=True
        temp_dict['footprint']=foot_flag
        temp_dict['category_name']=d.cat_id
        temp_dict['payload']=d.payload
        temp_dict['up_votes']=d.up_votes
        temp_dict['down_votes']=d.down_votes
        data2.append(temp_dict)
        break

    
    res11=db.session.execute('''select title from category where id="%s"'''%temp_dict['category_name'])
    for a in res11:
        cat_name=a[0]
        break  

    temp_dict['category_name']=cat_name   
    

    return {"payload":data2}



    








