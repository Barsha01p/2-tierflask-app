from flask import Flask, jsonify
import os
import pymysql

app = Flask(__name__)

# This is our homepage route
@app.route('/')
def home():
    return "<h1>Welcome to my Two-Tier Web Application!</h1><p>Visit /db-check to test the database connection tier.</p>"

# This is our backend tier testing route
@app.route('/db-check')
def check_database():
    try:
        # These variables act as dynamic connection placeholders
        connection = pymysql.connect(
            host=os.environ.get('DB_HOST', 'localhost'),
            user='root',
            password=os.environ.get('DB_PASSWORD', 'rootpassword'),
            database=os.environ.get('DB_NAME', 'my_app_db'),
            connect_timeout=3
        )
        return jsonify({"status": "Success", "message": "Connected to the MySQL database tier smoothly!"})
    except Exception as e:
        # Captures the error safely when the database isn't running yet
        return jsonify({"status": "Failed", "message": f"Could not connect to database tier: {str(e)}"}), 500

if __name__ == '__main__':
    # host='0.0.0.0' allows external traffic to reach the app later in Docker and AWS
    app.run(host='0.0.0.0', port=5000)

