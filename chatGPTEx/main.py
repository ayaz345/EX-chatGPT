import json
import random
import datetime
import time
from search import search,APIQuery,APIExtraQuery,Summary,SumReply,directQuery,web,detail,webDirect
# Load the configuration file


def parse_text(text):
    lines = text.split("\n")
    for i,line in enumerate(lines):
        if "```" in line:
            items = line.split('`')
            if items[-1]:
                lines[i] = f'<pre><code class="{items[-1]}">'
            else:
                lines[i] = f'</code></pre>'
        else:
            if i>0:
                line = line.replace("<", "&lt;")
                line = line.replace(">", "&gt;")
                lines[i] = '<br/>'+line.replace(" ", "&nbsp;")
    return "".join(lines)
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    mode = str(request.args.get('mode'))
    userText = str(request.args.get('msg'))
    now = datetime.datetime.now()
    if mode=="chat":
        q = str(userText)
        
        res = parse_text(directQuery(q))
        return res
    elif mode == "web":
        q = 'current Time: '+ str(now) + ' Query:'+ str(userText)
        res = parse_text(web(q))
        return res
    elif mode == "detail":
        q = 'current Time: '+ str(now) + ' Query:'+ str(userText)
        res = parse_text(detail(q))
        return res
    elif mode =='webDirect':
        q = 'current Time: '+ str(now) + ' Query:'+ str(userText)
        res = parse_text(webDirect(q))
        return res
    return "Error"
if __name__ == "__main__":
    app.run()