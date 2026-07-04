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
         with connection.cursor() as cursor:
            # 1. Create a physical table if it doesn't exist yet
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS system_logs (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    message VARCHAR(255)
                )
            """)
            
            # 2. Insert a test log entry
 cursor.execute("INSERT INTO system_logs (message) VALUES ('Jenkins deployment connection verified')")
            connection.commit()
            
            # 3. Read the data back to confirm it works
            cursor.execute("SELECT COUNT(*) FROM system_logs")
            count = cursor.fetchone()[0]

        return jsonify({
            "status": "Success", 
            "message": f"Connected smoothly! Total persistent logs recorded: {count}"
        })
    except Exception as e:
        return jsonify({"status": "Failed", "message": f"Could not connect to database tier: {str(e)}"}), 500
    finally:
        if 'connection' in locals() and connection.open:
            connection.close()
            
if __name__ == '__main__':
    # host='0.0.0.0' allows external traffic to reach the app later in Docker and AWS
    app.run(host='0.0.0.0', port=5000)

