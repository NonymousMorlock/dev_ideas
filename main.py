import json

from meter import Meter

# Receive data from me like this

request = open('tank_creation.json', 'r')

data = json.load(request)

request.close()

# Create tank and add to server like you do, and now we have the tank id

tank_id = 1

# create meters with that tank_id

number_of_meters = data['number_of_meters']

for i in range(number_of_meters):
    meter = Meter(
        meter_name=f'Meter {i}',
        starting_meter_reading=None,
        current_meter_reading=None,
        litre_rate=None,
        tank_id=tank_id
    )
    meter.meter_id = 1  # any way you generate your ids
    # add meter to database


'''but basically, the idea is that these things can be null at first, and later on, we can update them.

I can send you a put for updating the meter readings, and you can update the database with that.
PUT /starting_meter_reading/meter_id

{ starting_meter_reading: 1000 }
'''



