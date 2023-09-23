Blockchain for Automobile Parts 
====================

In this activity, you will learn to create a block class and show block data on the UI.

<img src= "https://media.slid.es/uploads/1525749/images/10651565/project.gif" width = "700" height = "300">




* Follow the given steps to complete this activity.


* Step 1: Create the Block Class


* Open file blockchain.py.


* Create the constructor using the __init__ function and pass the attributes index, timestamp, transaction, and previousHash.


    ` def __init__(self, index, timestamp, transaction, previousHash): `
`


* Store index, transaction, timeStamp, and previousHash in the respective object variables.


    ` self.index = index`

    `         self.transaction = transaction`
    
    `         self.timestamp = timestamp`
    
    `         self.previousHash = previousHash`

    `   self.currentHash = self.calculateHash() ` 
            `


* Step 2: Create the newBlock with Data


* Open file app.py.


* Create the newBlock using the data stored in the blockData.


    ` newBlock = Block(`

    ` blockData["index"], `

    ` blockData["timestamp"], `

    ` blockData["transaction"], `

    ` blockData["previousHash"]) `


* Pass the newBlock data to the index.html file in the variable blockData to display the data.


    ` return render_template('index.html', blockData = newBlock) `
        `


* Step 3: Display the Block Data on the Web page


* Open the file index.html from the template folder.


* Display the Block Number, Vendor, and Receiver data, which is received from the blockData object, in the specific fields of the webpage.



    ` <div class="header-data"style="margin-left: 40px; font-size: 1vw;">  `

    `	  <b>Block Number:</b> <span>#{{blockData.index}}</span> <br> `

    ` 	  <b>Vendor:</b><span>{{blockData.transaction['vendor']}}</span><br>`


    `	  <b>Receiver:</b><span>{{blockData.transaction['receiver']}}</span>         <br>`

    `     </div>`


* In a collapsible format, you can show or hide part number, part name, dimensions, weight, and timestamp attributes from the blockData.


    ` <div class="accordion-body">`

    `		<strong>Part Number:</strong> <span>{{blockData.transaction['partNumber']}}</span><br>`

    `		<strong>Part Name:</strong> <span>{{blockData.transaction['partName']}}</span><br> `

    `		<strong>Dimensions:</strong> <span>{{blockData.transaction['dimensions']}}</span><br>`

    `		<strong>Weight:</strong> <span>{{blockData.transaction['weight']}}</span><br>`

    `		<strong>Valid Block:</strong> <span>{{blockData.isValid}}</span><br>`
    
    `		<strong>Timestamp:</strong> <span>{{blockData.timestamp}}</span><br>`

    `						</div> `
                            `




* Save and run the code to check the output.
