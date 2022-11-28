import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import numpy as np

engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base ()
# reflect the tables
Base.prepare(engine,reflect=True)
# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station
session=Session(engine)
app = Flask(__name__)
##precep_dict = {"Date": "Precipitation (Inches)"}
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
    "Converting the query results to a dict"
    oneyr_date = dt.date(2017,8,23)-dt.timedelta(days=365)


    precip_score = session.query(measurement.date,measurement.prcp).filter(measurement.date >=oneyr_date).all()
    precep_dict = {date:prcp for date,prcp in precip_score}
    return jsonify(precep_dict)

@app.route("/api/v1.0/stations")
def stations():
    ##pu††ing station into list
    station_list = session.query(station.station).all()
    stations=list(np.ravel(station_list))
    return jsonify(stations=stations)
@app.route("/api/v1.0/tobs")
def tobs():
    prev_year  = dt.date(2017,8,23)-dt.timedelta(days=365)
    results=session.query(measurement.tobs).filter(measurement.station=="USC00519281").filter(measurement.date >=prev_year).all()
    tobs=list(np.ravel(results))
    return jsonify(tobs=tobs)





@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start=None,end=None):
    sel=[func.min(measurement.tobs),func.avg(measurement.tobs),func.max(measurement.tobs)]

    if not end:
        start=dt.datetime.strptime(start,"%m%d%Y")
        results=session.query(*sel).filter(measurement.date>=start).all()
        temps=list(np.ravel(results))
        return jsonify (temps)

    start=dt.datetime.strptime(start,"%m%d%Y")
    end=dt.datetime.strptime(start,"%m%d%Y")
    results=session.query(*sel).filter(measurement.date>=start).filter(measurement.date<=end).all()
    temps=list(np.ravel(results))
    return jsonify (temps)

if __name__ == "__main__":
    app.run(debug=True)

