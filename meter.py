class Meter(object):
    def __init__(self, meter_name, starting_meter_reading, current_meter_reading, litre_rate, tank_id):
        self.meter_name = meter_name
        self.starting_meter_reading = starting_meter_reading
        self.current_meter_reading = current_meter_reading
        self.litre_rate = litre_rate
        self.tank_id = tank_id
        self.meter_id = None
