from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_connection

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required
)

import bcrypt


app = Flask(__name__)

CORS(app)


# JWT Configuration
app.config["JWT_SECRET_KEY"] = "lead-desk-secret-key"

jwt = JWTManager(app)



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




# -----------------------------
# PUBLIC LEAD SUBMISSION
# -----------------------------

@app.route("/api/leads", methods=["POST"])
def create_lead():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    budget = data.get("budget")
    message = data.get("message")


    # Server-side validation
    if not name or not email or not budget or not message:

        return jsonify({
            "error": "All fields are required"
        }),400



    try:

        connection = get_connection()


        with connection.cursor() as cursor:

            sql = """
            INSERT INTO leads
            (name,email,budget,message)
            VALUES (%s,%s,%s,%s)
            """


            cursor.execute(
                sql,
                (
                    name,
                    email,
                    budget,
                    message
                )
            )


        connection.commit()
        connection.close()


        return jsonify({

            "message":"Lead submitted successfully!"

        }),201



    except Exception as e:


        return jsonify({

            "error":str(e)

        }),500






# -----------------------------
# ADMIN LOGIN
# -----------------------------

@app.route("/api/admin/login", methods=["POST"])
def admin_login():


    data = request.get_json()


    email = data.get("email")
    password = data.get("password")


    if not email or not password:

        return jsonify({

            "error":"Email and password required"

        }),400



    try:

        connection = get_connection()


        with connection.cursor() as cursor:


            cursor.execute(

                """
                SELECT *
                FROM admins
                WHERE email=%s
                """,

                (email,)

            )


            admin = cursor.fetchone()



        connection.close()



        if admin:


            stored_password = admin["password"].encode("utf-8")


            if bcrypt.checkpw(

                password.encode("utf-8"),

                stored_password

            ):


                token = create_access_token(

                    identity=email

                )


                return jsonify({

                    "token":token

                }),200




        return jsonify({

            "error":"Invalid credentials"

        }),401



    except Exception as e:

        print("LOGIN ERROR:", e)

        return jsonify({

            "error":str(e)

        }),500







# -----------------------------
# GET ALL LEADS (PROTECTED)
# -----------------------------

@app.route("/api/leads", methods=["GET"])
@jwt_required()
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



        return jsonify(leads),200




    except Exception as e:


        return jsonify({

            "error":str(e)

        }),500







# -----------------------------
# UPDATE STATUS (PROTECTED)
# -----------------------------

@app.route("/api/leads/<int:lead_id>", methods=["PUT"])
@jwt_required()
def update_lead_status(lead_id):


    data = request.get_json()


    status = data.get("status")



    if status not in [

        "New",
        "Contacted",
        "Closed"

    ]:


        return jsonify({

            "error":"Invalid status"

        }),400




    try:


        connection = get_connection()



        with connection.cursor() as cursor:


            sql = """

            UPDATE leads
            SET status=%s
            WHERE id=%s

            """


            cursor.execute(

                sql,

                (
                    status,
                    lead_id
                )

            )



        connection.commit()

        connection.close()



        return jsonify({

            "message":
            "Status updated successfully!"

        }),200




    except Exception as e:


        return jsonify({

            "error":str(e)

        }),500





if __name__ == "__main__":

    app.run(debug=True)