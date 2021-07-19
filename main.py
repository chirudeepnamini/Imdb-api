from fastapi import FastAPI,Path

from fastapi.encoders import jsonable_encoder
from typing import Optional
import secrets,sqlite3



app = FastAPI()

def data_from_db(db_name,stmt):
    conn=sqlite3.connect(db_name)
    cr=conn.cursor()
    cr.execute(stmt)
    result=cr.fetchall()
    return result


@app.get("/get-random-movie/{rating}")
async def fun(rating:int=Path(5,title="sth",le=9,ge=5),numVotes:int=5000):
    
    db_table={5:["data5.db","ratings_gt5"],6:["data6.db","ratings_gt6"],7:["data7.db","ratings_gt7"],8:["data8.db","ratings_gt8"],9:["data9.db","ratings_gt9"]}
    result=data_from_db(db_table[rating][0],f"select * from {db_table[rating][1]} where numVotes>="+str(numVotes))
    if(len(result)==0):
        return {"Error": "can't find any movie,decrease numVotes"}
    index=secrets.randbelow(len(result))
    print(result[index])
    link="https://www.imdb.com/title/"+result[index][0]
    return {"link":link,"averageRating":result[index][1],"numVotes":result[index][2]}

