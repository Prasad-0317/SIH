from urllib import response
import csv 
from datetime import datetime as dt
comments=[]
today = dt.today().strftime("%d-%m-%Y")

def process_comments(response_items,csv_op=False):
    for res in response_items:
        # handle non replies
        if 'replies' not in res.keys():
            comment={}
            comment['snippet']=res['snippet']['topLevelComment']['snippet']
            comment['commentId']=res['snippet']['topLevelComment']['id']
            comments.append(comment['snippet'])

        # print(comments)
    if csv_op:
        make_csv(comments)
    print(f'Finished processing {len(comments)} comments.')
    
    return comments

def make_csv(comments,channelID=None):
    header = comments[0].keys()
    if channelID:
        filename = f'comments_{channelID}_{today}.csv'
    else:
        filename = f'comments_{today}.csv'
    
    with open(filename,'w',encoding='utf8',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=header)
        writer.writeheader()
        writer.writerows(comments)
    
    