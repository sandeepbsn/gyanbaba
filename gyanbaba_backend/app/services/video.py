from ..models import db
from ..models.ResourceModel import Resource 
from ..models.CategoryModel import Category 
from ..models.FootprintModel import Footprint 
from  sqlalchemy.sql.expression import func

import random


def get_video(user_channel_id):
    
    res=Category.query.filter(Category.title=="video").all()
    # res=db.session.execute('select id from category where title="video"')
    for a in res:
        cat_id=a.id
        break

    # res1=db.session.execute('''select id from user where user_channel_id="%s"'''%channel_id)
    # for a in res1:
    #     user_id=a[0]
    #     break   

    res2=Footprint.query.filter(Footprint.user_id==user_channel_id).all()
    # res2=db.session.execute('select resource_id from footprint where user_id="%s"'''%user_channel_id)
    all_res=[]
    for a in res2:
        all_res.append(a.resource_id)

    print('-------------**********------------',all_res)

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
        

    if res2:
        foot=Footprint(resource_id=res_id,user_id=user_channel_id)
        db.session.add(foot)
        db.session.commit()

        return {"payload":data2}
    else:
        return {"payload":[{"flag":False,"payload":{"text":"NOTHING NEW FOR TODAY"}}]}
        




    # res=db.session.execute('select id from category where title="video"')
    # for a in res:
    #     cat_id=a[0]
    #     break

    
    # results=db.session.execute('select * from resource where cat_id="%s" ORDER BY RAND() LIMIT 1'%cat_id)
    
    
    # # print(results)
    
    # for result in results:
    #     # print(result['payload'])
    #     res_id=result['id']
    #     data=(result['payload'])
        
    # #     break

    # res={"res_id":res_id,"payload":data} 
    
    

    # return {"payload":res}


    

