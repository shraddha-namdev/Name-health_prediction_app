from ml_model import predict_health   # 👈 THIS LINE (add here)

from flask import Flask, render_template, request, redirect
from models import db, Patient
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Health prediction function
# Blood test values ke basis par remark generate karega
#
# def predict_health(glucose, hb, cholesterol):

#     if glucose > 140:
#         return "High Risk of Diabetes"

#     elif cholesterol > 240:
#         return "High Cholesterol Risk"

#     elif hb < 12:
#         return "Possible Anemia"

#     else:
#         return "Normal Health Indicators"


@app.route("/")
def home():

    patients = Patient.query.all()

    return render_template(
        "index.html",
        patients=patients
    )

# Add Patient Route
# GET = Form dikhana
# POST = Form data save karna
@app.route("/add", methods=["GET", "POST"])
def add_patient():
    # Agar user form submit kare

    if request.method == "POST":
        # Form se patient details lena

        full_name = request.form["full_name"]
        dob = request.form["dob"]
        email = request.form["email"]
        # Blood test values lena

        glucose = float(request.form["glucose"])
        haemoglobin = float(request.form["haemoglobin"])
        cholesterol = float(request.form["cholesterol"])


        # ---------------- VALIDATION (IMPORTANT) ----------------
        if glucose <= 0 or haemoglobin <= 0 or cholesterol <= 0:
            return "Invalid input values"
        # Prediction function call karna

        remarks = predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )
        # Patient object create karna

        patient = Patient(
            full_name=full_name,
            dob=dob,
            email=email,
            glucose=glucose,
            haemoglobin=haemoglobin,
            cholesterol=cholesterol,
            remarks=remarks
        )

        db.session.add(patient)      # Database me record add karna

        db.session.commit()#        # Changes save karna

        return redirect("/")#        # Save hone ke baad home page par redirect


    return render_template("add_patient.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_patient(id):

    patient = Patient.query.get(id)

    if request.method == "POST":

        patient.full_name = request.form["full_name"]
        patient.email = request.form["email"]

        patient.glucose = float(request.form["glucose"])
        patient.haemoglobin = float(request.form["haemoglobin"])
        patient.cholesterol = float(request.form["cholesterol"])

        patient.remarks = predict_health(
            patient.glucose,
            patient.haemoglobin,
            patient.cholesterol
        )

        db.session.commit()

        return redirect("/")

    return render_template(
        "edit_patient.html",
        patient=patient
    )


@app.route("/delete/<int:id>")
def delete_patient(id):

    patient = Patient.query.get(id)

    db.session.delete(patient)
    db.session.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)