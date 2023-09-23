from flask import Flask, render_template, request
import os
from hash import generateHash
from time import time
from blockchain import Block

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

blockData={}
encryptedData ={}

@app.route("/", methods= ["GET", "POST"])
def home():
    print("running")
    print(request.args.get("form"))
    global blockData, encryptedData
    if request.method == "GET":
        return render_template('index.html')
    elif request.args.get("form") == "f1":
        vendor = request.form.get("vendor")
        receiver = request.form.get("receiver")
        partName = request.form.get("partname")
        partNumber = request.form.get("partnumber")
        dimensions = request.form.get("dimensions")
        weight = request.form.get("weight")

        originalData = { 
                "vendor": vendor, 
                "receiver": receiver, 
                "partName": partName,
                "partNumber" : partNumber,
                "dimensions":dimensions,
                "weight":weight
            }
        
        vendor = generateHash(vendor)
        receiver = generateHash(receiver)
        
        transaction = { 
                "vendor": vendor, 
                "receiver": receiver, 
                "partName": partName,
                "partNumber" : partNumber,
                "dimensions":dimensions,
                "weight":weight
            }
        
        blockData = {
                'index': 1,
                'timestamp': time(),
                'transaction': transaction,
                'previousHash': "No Previous Hash Present. Since this is the first block.",
            }

        # Create newBlock using Block class
        newBlock = Block(
                        blockData["index"], 
                        blockData["timestamp"], 
                        blockData["transaction"],
                        blockData["previousHash"])
        
    # Pass newBlock as blockData
    return render_template('index.html', blockData = newBlock)
    
if __name__ == '__main__':
    app.run(debug = True, port=4000)