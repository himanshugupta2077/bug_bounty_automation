# customizing_kali
Creating a shell script that can be run after a fresh Kali install to tweak it as per personal preference. Inspired by pimpmykali from Dewalt-arch. (https://github.com/Dewalt-arch/pimpmykali) After that it will start running recon tools, save the ouput in txt and then will be added in the mongodb.

## workflow

1. open fresh kali

2. run tweak.sh
- system update
- add new user

3. log in as new user
- install new applications
	- sublime
 	- terminator
	- mongodb

4. run run.sh
- start mongodb service
- python -m pip install pymongo

5. run recon.py
- save in formatted txt files that matches documents in mongo.py

6. run mongo.py
- connect as admin
- create new user
- dissconnect

- connect as new user
- make new db (ronindb)

- make new collection (collec_tool_result)
- make new document (doc_tool_result)

- save tool output in a txt that follows doc_tool_result format like this:<br>
`field1 = 'value1'`<br>
`field2 = 'value2'`<br>

- insert data from this txt file in doc_tool_result like this:<br>
`doc_tool_result['field1'] = value1`<br>
`doc_tool_result['field2'] = value2`<br>

- now, insert the document doc_tool_result into the collec_tool_result<br>
`collec_tool_result.insert_one(doc_tool_result)`<br>

- dissconnect

