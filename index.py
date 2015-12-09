import web
import json
# -*- coding: utf-8 -*-
# Create your views here.
from api import NetEase
def get_song_infos():
       n = NetEase()
       songlist = []
       for i in n.top_songlist():
              singers = ""
              for t in[j['name'] for j in i['artists']]:
                     singers = singers+" "+t
              
              songlist.append([i['name'],singers,i['mp3Url']])
       return songlist

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return json.dumps(get_song_infos())

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
    
