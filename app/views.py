# -*- coding: utf-8 -*-

from flask import render_template #This is so the app can use html templates
from app import app


@app.route('/')
@app.route('/index')
def index():  #This is the landing page
	#Lessons, badges, and code are stored here as an array, but will be replaced by a database call sorted for order.
	weeks = [{'number':1,'title':'Radical Welcomings'}]
	lessons = [{'week':1, 'day':1, 'title': "Code, Power, and the Big Picture: Why us and why now?"},{'week':1, 'day':2, 'title':"Setting Up for (a) Movement: Staying healthy and happy while we learn and work"},{'week':1, 'day':3, 'title': "Master's Tools, Remastered Tools, Native Tools: Critical-conceptual app design using what we know about the world"},{'week':1, 'day':4, 'title': u"Our Compañeros: Meeting our larger community of support"}, {'week':1, 'day':5, 'title': "Relax, Reboot, Reimagine: Visioning and planning the tools we'll build in this program"}]
	badges = [{'category':'BASH', 'number':1,'name':'The Niobe'},{'category':'Python', 'number':1,'name':'The Snake Egg'},{'category':'Movement', 'number':1,'name':'The Upswing'}]
	code_samples = [{'name': 'This is nothing!', 'language': 'English', 'developer': {'firstname':'Aliya','lastname':'Rahman'}}]
	return render_template("index.html", weeks=weeks,lessons = lessons, badges = badges, code_samples=code_samples)