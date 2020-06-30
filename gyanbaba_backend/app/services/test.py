from ..models import db
from ..models.ResourceModel import Resource 
from ..models.CategoryModel import Category 
from ..models.FootprintModel import Footprint 
import random
from  sqlalchemy.sql.expression import func


def get_test1(channel_id):


    res=db.session.execute('select id from category where title="quote"')
    for a in res:
        cat_id=a[0]
        break

    res1=db.session.execute('''select id from user where user_channel_id="%s"'''%channel_id)
    for a in res1:
        user_id=a[0]
        break   

    res2=db.session.execute('select resource_id from footprint where user_id="%s"'''%user_id)
    all_res=[]
    for a in res2:
        all_res.append(a[0])

    # all_res=tuple(all_res)
    print('*******||||||||||||||************||||||||||||*********',all_res)
    s=''
    for a in all_res:
        s=s+str(a)+','
    data=({"cat_id":cat_id,"all_res":s})
    # all_res=tuple(all_res)
    results=db.session.execute('''select * from resource where cat_id=:cat_id AND id NOT IN (:all_res) ORDER BY RAND() LIMIT 1''',data)
    # results=Resource.query().filter(cat_id=cat_id,id.notin_(all_res)).all()
    
    # print(results)
    data={}
    for result in results:
        # print(result['payload'])
        res_id=result['id']
        data=(result['payload'])
        break
        

    res={"res_id":res_id,"item":data} 
    print('****&&&&&****&&&&&**&&&&&&',res_id)
    foot=Footprint(resource_id=res_id,user_id=user_id)
    db.session.add(foot)
    db.session.commit()

    return {"payload":res}


    
def get_test(channel_id):

    res=db.session.execute('select id from category where title="quote"')
    for a in res:
        cat_id=a[0]
        break

    res1=db.session.execute('''select id from user where user_channel_id="%s"'''%channel_id)
    for a in res1:
        user_id=a[0]
        break   

    res2=db.session.execute('select resource_id from footprint where user_id="%s"'''%user_id)
    all_res=[]
    for a in res2:
        all_res.append(a[0])

    print('-------------**********------------',all_res)

    # n=[2,3]
    res2=Resource.query.filter(~Resource.id.in_(all_res)).order_by(func.rand()).limit(1).all()
    data2=[]
    
    for d in res2:
        temp_dict={}
        res_id=d.id
        temp_dict['id']=d.id
        temp_dict['flag']=True
        temp_dict['payload']=d.payload
        temp_dict['up_votes']=d.up_votes
        temp_dict['down_votes']=d.down_votes

        data2.append(temp_dict)
        

    if res2:
        foot=Footprint(resource_id=res_id,user_id=user_id)
        db.session.add(foot)
        db.session.commit()

        return {"payload":data2}
    else:
        return {"payload":[{"flag":False,"payload":{"text":"NOTHING NEW FOR TODAY"}}]}
        



    
