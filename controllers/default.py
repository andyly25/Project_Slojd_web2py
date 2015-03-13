# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import indexmod
import haikumake
def index():
    haiku1 = haikumake.createHaiku1()
    haiku2 = haikumake.createHaiku2()
    return dict(haiku1=haiku1, haiku2=haiku2)

def randomHaiku():
    haiku2 = haikumake.createHaiku2()
    return dict(haiku2=haiku2)

def randomness (n):
    # import random
    line = ""
    while (n > 0):
        temp = indexmod.randint(1, n)
        line = line + str(temp)
        n-=temp
    return line


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
