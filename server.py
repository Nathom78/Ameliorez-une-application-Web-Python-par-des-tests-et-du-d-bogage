import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime


def loadClubs():
    """This function allows to load the clubs in de database."""
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    """This function allows to load the competitions in de database."""
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


app = Flask(__name__)
app.config.from_object('config')

competitions = loadCompetitions()
clubs = loadClubs()


@app.route("/")
def index():
    """This is the endpoint for the index page of the app"""
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    """This is the endpoint for the summary page of the app, where you can choose a competition to book places."""
    try:
        club = [club for club in clubs if club["email"] == request.form["email"]][0]
        return render_template("welcome.html", club=club, competitions=competitions)
    except IndexError:
        flash("unknown email, try again")
        return render_template("index.html")


@app.route("/book/<competition>/<club>", methods=["POST", "GET"])
def book(competition, club):
    """
    This is the enpoint for the page of the app where you can book a certain amount of places
    to the competition that you chose.
    """
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]
    dateNow = datetime.now().replace(microsecond=0)
    competitionDate = datetime.strptime(foundCompetition["date"], '%Y-%m-%d %H:%M:%S')
    if foundClub and foundCompetition:
        if dateNow <= competitionDate:
            return render_template("booking.html", club=foundClub, competition=foundCompetition)
        else:
            flash("sorry, this competition already took place")
            return render_template('welcome.html', club=foundClub, competitions=competitions)
    else:
        flash("Something went wrong-please try again")
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    """
    This function allows you to validate a reservation of places to a competition and
    redirect to the summary with new datas.
    """
    competition = [c for c in competitions if c["name"] == request.form["competition"]][0]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    placesRequired = int(request.form["places"])
    if (placesRequired <= 12) and (int(club["points"]) - placesRequired) >= 0:
        competition["numberOfPlaces"] = int(competition["numberOfPlaces"]) - placesRequired
        club["points"] = int(club["points"]) - placesRequired
        flash("Great-booking complete!")
    elif int(club["points"]) - placesRequired < 0:
        flash("sorry, you do not have enough points", category='error')
    elif placesRequired > 12:
        flash("Sorry, you cannot book more than 12 places.", category='error')
    return render_template("welcome.html", club=club, competitions=competitions)


# TODO: Add route for points display

@app.route("/logout")
def logout():
    """This endpoint is the logout of the application"""
    return redirect(url_for("index"))
