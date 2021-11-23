from flask import Flask, request

from main import insertSite

app = Flask("whois")


@app.route("/whois", methods=["GET"])
def testewhois():
    return {"teste": "whois"}


@app.route("/cadastra/Site", methods=["POST"])
def cadastrasite():

    body = request.get_json()

    site = insertSite(body["site"])

    return site

app.run()