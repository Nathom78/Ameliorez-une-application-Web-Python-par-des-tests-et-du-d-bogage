import json
from flask import Flask, render_template, request, redirect, flash, url_for


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


competitions = loadCompetitions()
clubs = loadClubs()

app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
def index():
    """This is the endpoint for the index page of the app"""
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    """This is the endpoint for the summary page of the app, where you can choose a competition to book places."""
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route("/book/<competition>/<club>")
def book(competition, club):
    """
    This is the enpoint for the page of the app where you can book a certain amount of places
    to the competition that you chose.
    """
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]
    if foundClub and foundCompetition:
        return render_template("booking.html", club=foundClub, competition=foundCompetition)
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
    competition["numberOfPlaces"] = int(competition["numberOfPlaces"]) - placesRequired
    flash("Great-booking complete!")
    return render_template("welcome.html", club=club, competitions=competitions)


# TODO: Add route for points display
@app.route("/board", methods=["POST"])
def board():
    """This endpoints redirects you to a board display with the summary of each club's points"""
    return render_template("board.html", clubs=clubs)


@app.route("/logout")
def logout():
    """This endpoint is the logout of the application"""
    return redirect(url_for("index"))
