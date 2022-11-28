import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base ()
# reflect the tables
Base.prepare(engine,reflect=True)
# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)
precep_dict = {"Date": "Precipitation (Inches)"}
 @app.route("/")
 def welcome():
     "List all avaliable routes"
     return(
         f"/api/v1.0/precipitation"
         f"/api/v1.0/stations"
         f"/api/v1.0/tobs"
         f"/api/v1.0/<start>"
         f"api/v1.0/<start>/<end>"
     )

@app.route("/api/v1.0/precipitation")
def precepitation():
    "help"
    return jsonify(precipitation)

    if __name__ == "__main__":
    app.run(debug=True)

