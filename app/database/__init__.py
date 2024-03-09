import sqlite3
from flask import g  #g is global contecx object, will allow you to cache certain items

DATABASE_URL = "main.db"

def get_db():
    db = getattr(g, "_database", None)
    if not db: # if db is set to none
        db = g._database = sqlite3.connect(DATABASE_URL)
        return db