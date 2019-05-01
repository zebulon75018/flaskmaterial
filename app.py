# -*- coding:utf-8 -*-

import json

from flask import Flask, request, render_template
app = Flask(__name__)

app.debug = True
class Material:
    def __init__(self):
        pass

    def itemlist(self, what,who,when,notes):
        item = {"what":what,"who":who,"when":when,"notes":notes }
        return render_template('itemlist.html', item=item)

@app.route('/')
def index():
    menu = [
    {
      'link' : '',
      'title' :  'Dashboard',
      'icon' : 'dashboard',
    },
    {
      'link' : '',
      'title': 'Friends',
      'icon': 'group',
    },
    {
      'link' : '',
      'title': 'Messages',
      'icon': 'message'
    }
  ]

    activity = [
      {
        'what': 'Brunch this weekend?',
        'who': 'Ali Conners',
        'when': '3:08PM',
        'notes': " I'll be in your neighborhood doing errands"
      },
      {
        'what': 'Summer BBQ',
        'who': 'to Alex, Scott, Jennifer',
        'when': '3:08PM',
        'notes': "Wish I could come out but I'm out of town this weekend"
      },
      {
        'what': 'Oui Oui',
        'who': 'Sandra Adams',
        'when': '3:08PM',
        'notes': "Do you have Paris recommendations? Have you ever been?"
      },
      {
        'what': 'Birthday Gift',
        'who': 'Trevor Hansen',
        'when': '3:08PM',
        'notes': "Have any ideas of what we should get Heidi for her birthday?"
      },
      {
        'what': 'Recipe to try',
        'who': 'Brian Holt',
        'when': '3:08PM',
        'notes': "We should eat this: Grapefruit, Squash, Corn, and Tomatillo tacos"
      },
    ];
    return render_template('index.html', menu=menu,activity=activity, util= Material())

if __name__ == '__main__':
    app.run()