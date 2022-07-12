from app import app , Response, request, jsonify, json
from helpers.db_helpers import run_query

@app.get('/api/users')
def user_get():
    pass


@app.post('/api/users')
def user_post():
    user_resp = request.json
    email = user_resp.get('email')
    password = user_resp.get('password')
    username = user_resp.get('username')
    run_query('INSERT INTO users (email, password, username) VALUES (?,?,?)', [email,password,username])
    return jsonify('User created'), 200