from ..models import db
from ..models.ResourceModel import Resource 
from ..models.CategoryModel import Category 
from ..models.FootprintModel import Footprint 
from  sqlalchemy.sql.expression import func
import random
import datetime



def get_quote(user_channel_id):
    res=Category.query.filter(Category.title=="quote").all()
    # res=db.session.execute('select id from category where title="quote"')
    for a in res:
        cat_id=a.id
        break

    # res1=db.session.execute('''select id from user where user_channel_id="%s"'''%channel_id)
    # for a in res1:
    #     user_id=a[0]
    #     break   

    res2=Footprint.query.filter(Footprint.user_id==user_channel_id).filter().all()
    # res2=db.session.execute('select resource_id from footprint where user_id="%s"'''%user_channel_id)
    all_res=[]
    curr_timestamp = datetime.datetime.now()
    count_min = 0
    count_hr = 0
    flag = 0
    for a in res2:
        if count_min >= 2:
            flag = 1
            break
        com_timestamp = curr_timestamp.replace(microsecond=0)
        elapsed_time = com_timestamp - a.timestamp
        print('****** type',type(com_timestamp),type(a.timestamp),type(elapsed_time),elapsed_time)
        days = elapsed_time.days
        hours, remainder = divmod(elapsed_time.seconds,3600)
        minutes, seconds = divmod(remainder, 60)
        print(hours,minutes)
        

        #for not more than 3 request in a minute
        if days == 0:
            if hours == 0:
                if minutes <=1:
                    count_min +=1

        # for not more than 3 requests in an hour
        if days == 0:
            if hours == 0:
                count_hr +=1
        # if (a.timestamp).strftime("%H:%M:%S")>= '7:19:00' and (a.timestamp).strftime("%H:%M:%S") <= '8:19:00':
        #     count +=1
        all_res.append(a.resource_id)

    # print('-------------**********------------',count)
    if flag == 1:
        return {"payload":[{"flag":False,"payload":{"text":"GO & STUDY"}}]}
    else:
    # n=[2,3]
        res2=Resource.query.filter(Resource.cat_id.like(cat_id)).filter(~Resource.id.in_(all_res)).order_by(func.rand()).limit(1).all()
        data2=[]
        
        for d in res2:
            temp_dict={}
            res_id=d.id
            temp_dict['res_id']=d.id
            temp_dict['flag']=True
            temp_dict['payload']=d.payload
            temp_dict['up_votes']=d.up_votes
            temp_dict['down_votes']=d.down_votes

            data2.append(temp_dict)
            
        
        curr_timestamp = curr_timestamp.strftime("%Y-%m-%d %H:%M:%S")
        if res2:
            foot=Footprint(resource_id=res_id,user_id=user_channel_id,timestamp=curr_timestamp)
            db.session.add(foot)
            db.session.commit()

            return {"payload":data2}
        else:
            return {"payload":[{"flag":False,"payload":{"text":"NOTHING NEW FOR TODAY"}}]}
            




    # res=db.session.execute('select id from category where title="quote"')
    # for a in res:
    #     cat_id=a[0]
    #     break

    
    # results=db.session.execute('select * from resource where cat_id="%s" ORDER BY RAND() LIMIT 1'%cat_id)
    
    
    # # print(results)
    # data={}
    # for result in results:
    #     # print(result['payload'])
    #     res_id=result['id']
    #     data=(result['payload'])
    #     up_votes=result['up_votes']
    #     down_votes=result['down_votes']

        

    # res={"res_id":res_id,"payload":data,"up_votes":up_votes,"down_votes":down_votes} 

    

    # return {"payload":res}


    

