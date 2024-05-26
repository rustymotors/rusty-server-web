from flask import Flask, request, make_response
from rusty_server_web.service.shard import getShardList
from rusty_server_web.util import formatShardEntriesForWeb

app = Flask(__name__)

@app.route("/AuthLogin")
def authlogin():
    username = request.args.get('username') 
    response = make_response(f"Valid=TRUE\nTicket={username}")
    response.headers['Content-Type'] = 'text/plain'   
    return response

@app.route("/ShardList/")
def shardlist():
    
    shardList = getShardList()
    
    response = make_response(formatShardEntriesForWeb(shardList))
    response.headers['Content-Type'] = 'text/plain'   
    return response
