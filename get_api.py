#Implementing the get id
from flask import Flask, jsonify

app=Flask(__name__)

Nepal=[{

"name":"province 1",
"capital":"biratnagar",
"CM":"rai",
},

{

"name":"province 2",
"capital":"janakpur",
"CM":"pandit",
},

{

"name":"province 3",
"capital":"hetauda",
"CM":"ppp",
},

{

"name":"province 4",
"capital":"pokhara",
"CM":"magar",
}
,
{

"name":"province 5",
"capital":"dang",
"CM":"pokhrel",
}
,
{

"name":"province 6",
"capital":"surkhet",
"CM":"shai",
}
,
{

"name":"province 7",
"capital":"dhangadi",
"CM":"bhatta",
}
]



@app.route('/')

def index():
 return "welcome to the course API"
@app.route("/Nepal",methods=['GET'])

def get():
 return jsonify({'NP':Nepal})

@app.route("/Nepal/<string:CM>",methods=['GET'])

def get_state(CM):
 return jsonify({'NP':Nepal[CM]}) 

if __name__ == "__main__":
 app.run(debug=True)
  

