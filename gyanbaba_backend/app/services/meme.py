from ..models import db
from ..models.ResourceModel import Resource 
from ..models.CategoryModel import Category 
from ..models.FootprintModel import Footprint 
from  sqlalchemy.sql.expression import func
import random
import datetime


def get_all_meme():
    
    res=Category.query.filter(Category.title=="meme").all()
    # res=db.session.execute('select id from category where title="quote"')
    for a in res:
        cat_id=a.id
        break

    # res1=db.session.execute('''select id from user where user_channel_id="%s"'''%channel_id)
    # for a in res1:
    #     user_id=a[0]
    #     break   

    # n=[2,3]
    res2=Resource.query.filter(Resource.cat_id.like(cat_id)).all()
    data2=[]
    
    for d in res2:
        # temp_dict={}
        #print('*********DATA MEME',d.payload)
        # temp_dict['payload']=d.payload
        data2.append(d.payload)
        
    print('getting meme data from backend')
    
    return {"payload":data2}
    
        




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


    

