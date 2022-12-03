from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitations<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def prcp():
    session = Session(engine)
    measurement = Base.classes.measurement
    date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= date).all()
    #results_prcp = session.query(measurement.date, measurement.prcp).all()
    session.close()

    precipitation = []
    for date, prcp in results:
        precipitation_dictionary = {date: prcp}
        precipitation.append(precipitation_dictionary)
   
    return jsonify(hawaiiprecipitation)


@app.route("/api/v1.0/stations")
def stationa():
    session = Session(engine)
    station = Base.classes.station
   
    results = session.query(station.name).all()
    results_list = list(np.ravel(results))
    session.close()

    return jsonify(results_list)

    return jsonify({"error": "Character not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)
    
@app.route("/api/v1.0/tobs)
def stationa():
    session = Session(engine)
    station = Base.classes.station
   
    results = session.query(station.name).all()
    results_list = list(np.ravel(results))
    session.close()

    return jsonify(results_list)

    return jsonify({"error": "Character not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)
    
