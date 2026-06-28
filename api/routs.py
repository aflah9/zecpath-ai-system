# api/routes.py

from flask import Flask, request, jsonify
from screening_ai.report_generator import generate_screening_report

app = Flask(__name__)

@app.route("/screening/start", methods=["POST"])
def start_screening():

    data = request.json

    report = generate_screening_report(
        data["candidate_id"],
        data["job_id"],
        data["answers"],
        data["scores"],
        data["behavior"]
    )

    return jsonify(report)