# Import needed libraries
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from datetime import datetime
from dateutil.relativedelta import relativedelta   

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# Reflect an existing database into a new model and table
Base = automap_base()
Base.prepare(engine, reflect=True)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Creating Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitations<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

# reate and query precipitation route and date values, create dictionary using date as the key and prcp as the value
@app.route("/api/v1.0/precipitation")
def precip():
    # create session/link from Python to the DB    
    session = Session(engine)
    measurement = Base.classes.measurement
    date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # query all measurements
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= date).all()
    session.close()
    # Create a dictionary from the row data and append to a list of  all_date_percp
    precipitation = []
    for date, prcp in results:
        precipitation_dictionary = {date: prcp}
        precipitation.append(precipitation_dictionary)
   
    return jsonify(hawaiiprecipitation)

# return JSON list of stations from the dataset, then create a dictionary to hold station data
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station = Base.classes.station
   
    results = session.query(station.name).all()
    results_list = list(np.ravel(results))
    session.close()

    return jsonify(results_list)

    return jsonify({"error": "Character not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)
    
# Query dates & temp observations for the most active station for the previous year of data.
@app.route("/api/v1.0/tobs")
def tobs()():
    # create session/link from Python to the DB 
    session = Session(engine)
    # measurement = Base.classes.measurement
    station = Base.classes.station
    # return JSON list of temperature observations (TOBS) for the previous year.   
    results = results.all()
    # create a dictionary from the row data and append to a list of  all_min_max_avg_date
    all_min_max_avg_date = []
    
#     for min, max, avg in results:
#         date_tobs_dict = {}
#         date_tobs_dict["TMIN"] = min  
#         date_tobs_dict["TMAX"] = max
#         date_tobs_dict["TAVG"] = avg   
#         all_min_max_avg_date.append(date_tobs_dict)
#     return jsonify(all_min_max_avg_date)

    results = session.query(station.name).all()
    final_output = list(np.ravel(results))
    session.close()

    return jsonify(final_output)

    return jsonify({"error": "Character not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)
    
