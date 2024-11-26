from flask import Flask, jsonify

app = Flask(__name__)

#  data
data = [
    {"id": 1, "name": "Alice", "role": "Engineer"},
    {"id": 2, "name": "Bob", "role": "Designer"},
    {"id": 3, "name": "Charlie", "role": "Manager"}
]
# here it get the json data in  /user
@app.route('/users',)
def get_users():
    return jsonify(data)
#checks if  a partficular name exist in the data and must be in lowercase
@app.route('/users/<name>', methods=['GET'])
def get_user_by_name(name):
    user = next((user for user in data if user['name'].lower() == name.lower()), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'})

if __name__ == '__main__':
    app.run(debug=True)
