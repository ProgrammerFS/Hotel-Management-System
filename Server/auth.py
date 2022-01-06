from flask import Blueprint, render_template, request, flash, redirect
import random
from .data import sign_up
from .data import log_in
auth = Blueprint(
    'auth', 
    __name__
)
def confirm_password(email, password):
    correct_password = log_in(email)
    confirmation = False
    if password==correct_password:
        confirmation=True
    return confirmation
@auth.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        data=request.form
        name = data.get("FirstName")
        email = data.get("email")
        password = data.get("password")
        x = confirm_password(email, password)
        if x==True:
            return redirect("http://127.0.0.1:5000/logged-in", code=302)
        else:
            flash("Sorry Wrong Password Please Try Again", category='error')
            return render_template("login.html", text="testing")
    elif request.method == "GET":
        return render_template("login.html", text="testing")

@auth.route("/logged-in", methods=["GET", "POST"])
def Logged_in():
    if request.method == "GET":
        return  render_template("logged_in.html")
    if request.method == "POST":
        name = request.form.get("Name")
        roomtype = request.form.get("roomtype")
        flash("Customer Checked-in ", category='success')
        
        return render_template("logged_in.html")

@auth.route("/logout")
def Logout():
    return render_template("logout.html")


@auth.route("/check-out", methods=["GET", "POST"])
def check_out():
     if request.method == "POST":
        name = request.form.get("Name")
        room = request.form.get("roomnumber")
        #
        return render_template("Details.html", Name=name, room = room, roomtype = "", check_in_time = "", check_out_time = "", amount="")

     else:
        return render_template("check-out.html")

