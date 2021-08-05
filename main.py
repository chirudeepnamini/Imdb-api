from fastapi import FastAPI,Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from typing import Optional
import sqlite3
import random,time

app = FastAPI()
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)
def data_from_db(db_name,stmt):
    print(stmt)
    conn=sqlite3.connect(db_name)
    cr=conn.cursor()
    cr.execute("SELECT * FROM sqlite_master WHERE type = 'table'")
    print(cr.fetchall())
    cr.execute(stmt)
    result=cr.fetchall()
    return result

@app.get("/get-random-movie/{rating}")
async def fun(rating:int=Path(5,title="sth",le=9,ge=5),numVotes:int=5000):
    start = time.time()
    db_table={5:["data5.db","ratings_gt5"],6:["data6.db","ratings_gt6"],7:["data7.db","ratings_gt7"],8:["data8.db","ratings_gt8"],9:["data9.db","ratings_gt9"]}
    result=data_from_db(db_table[rating][0],f"select * from {db_table[rating][1]} where numVotes>="+str(numVotes))
    duration = time.time() - start
    print('{0}s'.format(duration))
    if(len(result)==0):
        return {"Error": "can't find any movie,decrease numVotes"}
    movie=random.choice(result)
    print(movie)
    link="https://www.imdb.com/title/"+movie[0]
    return {"link":link,"averageRating":movie[1],"numVotes":movie[2],"tconst":movie[0]}
#c05n199l_TojD2ekkNnBAGApikRhNVef9jaS9pVL6
#c05n199l
# @app.get("/get-movie-info/{tconst}")
# async def info(tconst:str):
#     start = time.time()
#     result=data_from_db('movies_info_db.db',f"select * from movies_info where tconst='{tconst}'")
#     duration = time.time() - start
#     print('{0}s'.format(duration))
#     if(len(result)==0):
#         return {"Error": "can't find any movie,check your tconst"}
#     print(result)
#     print(type(result[0]))
#     return result[0]