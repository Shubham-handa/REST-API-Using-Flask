# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:26:40 2020

@author: Handa
"""

#importing libraries

from flask import Flask, request, json, Response
from pymongo import MongoClient
import logging as log
from waitress import serve

app = Flask(__name__) #Initialize the application

#Declaring class 

class MongoAPI:
    
    """In below function we are accepting information about Database and Collection from the user and initializing our database collection object through it.
    We are going to use this collection object throughout our code to read and manipulate data"""
    
    def __init__(self, data):
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')
        self.client = MongoClient("mongodb://<UserName>:<Password>@cluster0-shard-00-00.mxt87.gcp.mongodb.net:27017,cluster0-shard-00-01.mxt87.gcp.mongodb.net:27017,cluster0-shard-00-02.mxt87.gcp.mongodb.net:27017/<CollectionName>?ssl=true&replicaSet=atlas-17f95z-shard-0&authSource=admin&retryWrites=true&w=majority") #Creating MongoDB interactor for interacting with database where data is stored.   
        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data
        
        
    #This method will allow us to read all of the documents present in our collection
    def read(self):
        log.info('Reading All Data')
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents] #This line is used to reformat the data which we access from collection of MongoDB.
        return output #The output of the collection object is of datatype dictionary
    

    """his method will allow us to add a new document in MongoDB’s collection.
    Please note that we are accepting data from the user under the key 'Document'""" 
    def write(self, data):
        log.info('Writing Data')
        new_document = data['Document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output
    

    """This method allows us to update any existing documents. For this, we need to accept 2 details from the user.
    First is the filter on the basis of which we are going to select documents to be updated. Second is DataToBeUpdated"""
    
    def update(self):
        log.info('Updating Data')
        filt = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output
    

    """This method allows us to delete any existing documents. For this, we are accepting some filtering details form users to extract the documents to be deleted.
    Note that like update() we also have custom return messages depending on if something was deleted or not"""
    
    def delete(self, data):
        log.info('Deleting Data')
        filt = data['Filter']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output

#Define a single entry point so that we could verify that our server is working
#‘@app.route’ is a decorator that defines what endpoint is going to be accepted
        
@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')



#Defining CRUD HTTP Methods
#We are reading the data when a request is sent using the GET HTTP Method
    
@app.route('/mongodb', methods=['GET']) 
def mongo_read():
    data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.read()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


# We are writing the data when a request is sent using the POST HTTP Method
    
@app.route('/mongodb', methods=['POST'])
def mongo_write():
    data = request.json
    if data is None or data == {} or 'Document' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.write(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


"""We are updating the data when a request is sent using the PUT HTTP Method.
We have added a new field of “Filter” basis on which we determine which document needs to be updated"""

@app.route('/mongodb', methods=['PUT'])
def mongo_update():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.update()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


"""We are deleting the data when a request is sent using the DELETE HTTP Method.
We have added a new field of “Filter” basis on which we determine which document needs to be deleted"""

@app.route('/mongodb', methods=['DELETE'])
def mongo_delete():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.delete(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8005) #Define the ports and IP and start the server
