from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_connection

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Welcome to LeadDesk Mini Backend!"


@app.route("/test-db")
def test_db():
    try:
        connection = get_connection()
        connection.close()
        return "Database Connected Successfully!"
    except Exception as e:
        return f"Database Connection Failed: {str(e)}"


@app.route("/api/leads", methods=["POST"])
def create_lead():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    budget = data.get("budget")
    message = data.get("message")

    # Server-side validation
    if not name or not email or not budget or not message:
        return jsonify({"error": "All fields are required"}), 400

    try:
        connection = get_connection()

        with connection.cursor() as cursor:

            sql = """
                INSERT INTO leads
                (name, email, budget, message)
                VALUES (%s, %s, %s, %s)
            """

            cursor.execute(sql, (name, email, budget, message))

        connection.commit()
        connection.close()

        return jsonify({
            "message": "Lead submitted successfully!"
        }), 201

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

@app.route("/api/leads", methods=["GET"])
def get_leads():

    try:
        connection = get_connection()

        with connection.cursor() as cursor:

            sql = """
                SELECT *
                FROM leads
                ORDER BY created_at DESC
            """

            cursor.execute(sql)

            leads = cursor.fetchall()

        connection.close()

        return jsonify(leads), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

@app.route("/api/leads/<int:lead_id>", methods=["PUT"])
def update_lead_status(lead_id):

    data = request.get_json()

    status = data.get("status")

    if status not in ["New", "Contacted", "Closed"]:
        return jsonify({
            "error": "Invalid status"
        }), 400

    try:
        connection = get_connection()

        with connection.cursor() as cursor:

            sql = """
                UPDATE leads
                SET status=%s
                WHERE id=%s
            """

            cursor.execute(sql, (status, lead_id))

        connection.commit()
        connection.close()

        return jsonify({
            "message": "Status updated successfully!"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)