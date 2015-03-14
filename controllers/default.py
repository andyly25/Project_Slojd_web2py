# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import indexmod
import HaikuMake
import UserInputMatching

# Passes haiku type 2 to a variable that the html
# file can read and present
def index():
    haiku2 = HaikuMake.createHaiku2()
    return dict(haiku2=haiku2)

# Passes haiku type 1 to a variable that the html
# file can read and present
def pureRandomHaiku():
    haiku1 = HaikuMake.createHaiku1()
    return dict(haiku1=haiku1)

# Placeholder for the input file html page, returns nothing
def inputRandomHaiku():
    return dict()

# Defines a new post, which gets the 3 most recent entries
# into our database and passes them to the HaikuMake file which helps make our
# custom haiku
def new_post():
    form = SQLFORM(db.npost)
    if form.accepts(request, formname=None):
        getDbItem1 = db(db.npost.entry1!=None).select().last()
        getDbItem2 = db(db.npost.entry2!=None).select().last()
        getDbItem3 = db(db.npost.entry3!=None).select().last()

        wordItem1 = getDbItem1.entry1
        wordInfo1 = UserInputMatching.inputMatching(getDbItem1.entry1)
        if(wordInfo1[0] == 0):
            return DIV(wordItem1 + " is not in our dictionary!\nSorry, enter another word.")
        wordLine1 = createLine(wordItem1, wordInfo1, 5, 1)

        wordItem2 = getDbItem2.entry2
        wordInfo2 = UserInputMatching.inputMatching(getDbItem2.entry2)
        if(wordInfo2[0] == 0):
            return DIV(wordItem2 + " is not in our dictionary!\nSorry, enter another word.")
        wordLine2 = createLine(wordItem2, wordInfo2, 7, 2)

        wordItem3 = getDbItem3.entry3
        wordInfo3 = UserInputMatching.inputMatching(getDbItem3.entry3)
        if(wordInfo3[0] == 0):
            return DIV(wordItem3 + " is not in our dictionary!\nSorry, enter another word.")
        wordLine3 = createLine(wordItem3, wordInfo3, 5, 3)

        return DIV(wordLine1 + "\n" + wordLine2 + "\n" + wordLine3)
    elif form.errors:
        return TABLE(*[TR(k, v) for k, v in form.errors.items()])

# Accesses HaikuMake function that creates each line of the custom inputted haiku
def createLine(itemStr, itemInfo, sylCount, lineNum):
    return HaikuMake.createLine3(itemStr, itemInfo, sylCount, lineNum)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
