from flask import Flask
import urllib
from sqlalchemy import *


app = Flask(__name__)
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=IRIS-CSG-1634;DATABASE=JohnDoeBox;")
# engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
