import psycopg2
import requests
from flask import Flask, request, Response, json, g
from google.protobuf.json_format import MessageToDict
from protobuf import proto_measurements_pb2
import datetime
import base64


def server():
    app = Flask(__name__)
    # Enter your database credentials: database host, name, user and password
    DATABASE_HOST = 'host_name';
    DATABASE_USER = 'database_user';
    DATABASE_PASSWORD = 'database_password';
    DATABASE_NAME = 'database_name';

    # Making the initial connection:
    conn = psycopg2.connect(
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        host=DATABASE_HOST,
        password=DATABASE_PASSWORD
    )

    # Set up "/api/v2/measurements" endpoint, which will be receiving the data sent by Efento sensors
    @app.route('/api/v2/measurements', methods=['POST'])
    def respond():
        record = []

        for reports in request.json['reports']:
            data = MessageToDict(
                proto_measurements_pb2.ProtoMeasurements().FromString(bytearray.fromhex(reports['value'])))

            if list(data.keys())[0] == "serialNum":
                for measurement in data['channels']:
                    # creating a list of sensor parameters(measured_at, serial_number, battery_status) and measurements
                    for sampleOffsets in measurement['sampleOffsets']:
                        record.extend([(datetime.datetime.fromtimestamp(measurement['timestamp']),
                                        base64.b64decode((data['serialNum'])).hex(),
                                        data['batteryStatus'],
                                        measurement['type'], (measurement['startPoint'] + sampleOffsets) / 10)])

                    measurements = "INSERT INTO measurements(measured_at, serial_number, battery_ok, type, value) VALUES (%s, %s, %s, %s, %s)"
                    with conn.cursor() as cur:
                        try:
                            # inserting a list of sensor parameters and measurement to table in PostgresSQL
                            cur.executemany(measurements, record)
                            conn.commit()
                            cur.close()
                        except (Exception, psycopg2.DatabaseError) as error:
                            print(error)
                            return Response(status="500")
                    return Response(status='201')
            else:
                # returning response code 201
                return Response(status='201')

        return Response(status='201')

    # Start the application on Your port.Default port 5000
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    server()
