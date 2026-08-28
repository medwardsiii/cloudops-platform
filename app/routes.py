import os

from flask import Blueprint, jsonify

main = Blueprint ("main", __name__)

@main.route("/")
def home():
    return jsonify(
            application="CloudOps Platform",
            environment=os.getenv("APP_ENV", "development"),
            status="healthy",
            version=os.getenv("APP_VERSION", "1.0.0"),
    )


@main.route("/health")
def health():
    return jsonify(
            status="healthy"
    ), 200
