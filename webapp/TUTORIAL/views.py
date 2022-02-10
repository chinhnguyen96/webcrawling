from flask import  Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/chitietdoanhthu")
def report(): 
    return render_template("doanhthu.html")
