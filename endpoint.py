from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/question", methods=['POST'])
def endpoint():
    data = request.form
    print(data)
    output = f"""

<!doctype html>
<head>
    <title> Result </title>
    <style>
        .result {{
            color: rgb(179, 255, 208);
            font-family: "Lucida Console", "Courier New", monospace;
        }}
        .Title {{
            color: rgb(179, 255, 208);
            font-family: "Lucida Console", "Courier New", monospace;
            font-size: 40px;
        }}
        body {{
            background-color:black;
        }}

    </style>
</head>
<body>
    <div class='Title'>
    Results!!!
    </div>

    <br>

    <div class='result'>{data['NAME']} went to {data['PLACE']} with {data['FRIEND']}. 
    {data['FRIEND']} had a {data['COLOR']} {data['NOUN']} who {data['NAME']} hated. 
    He hated seeing {data['FRIEND']} with that {data['NOUN']} that he would like to imagine himself
    {data['VERB_ING']} {data['FRIEND']} in the {data['NOUN_2']}. {data['NAME']} would rather if {data['FRIEND']} 
    had a {data['ADJECTIVE']} {data['NOUN_3']} as he is a {data['PROFESSION']}.
    </div>
</body>
    """

    return output

@app.route("/", methods=['POST'])
def anotherfunction():
    pass

app.run(port=5000)



    #

    
    #  
    #