#put and delete - http verbs
#working with apis - json

from flask import Flask,jsonify,request
app = Flask(__name__)

#initial data in my to do list
items = [
    {"id":1,"name":"item 1","description":"this is the item 1"},
    {"id":2,"name":"item 2","description":"this is the item 2"}
]


@app.route('/')
def home():
    return "welcome to the sample to do list App"

#get:retreive all the items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)


#get:retrive the items based on id
@app.route('/items/<int:id>',methods = ['GET'])
def items_id(id):
    item = next((item for item in items if item['id'] == id), None)
    if item is None:
        return jsonify({"error":"item is not found"})
    return jsonify(item)

#post: create a new task
@app.route('/items',methods = ['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"items not found"})
    new_item = {
        "id":items[-1]["id"] + 1 if items else 1,
        "name":request.json['name'],
        "description":request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)


#put :update an existing item
@app.route('/items/<int:id>',methods = ['PUT'])
def update_item(id):
    item = next((item for item in items if item['id'] == id),None)
    if item is None:
        return jsonify({'error':'item not found'})
    item['name'] = request.json.get('name',item['name'])  #updating the name
    item['description'] = request.json.get('description',item['description'])   #updating the description
    return jsonify(item)

#DELETE :delelte an item
@app.route('/items/<int:id>',methods = ['DELETE'])
def delete_items(id):
    global items
    items = [item for item in items if item['id'] != id]
    return jsonify({"result":"item deleted"})

if __name__ =="__main__":
    app.run(debug= True)




#for after running this use the postman app for post,put,delete to see the changes
