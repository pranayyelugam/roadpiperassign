from my_app import db
 
class Pickups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float(asdecimal=True),index=True)
    longitude = db.Column(db.Float(asdecimal=True),index=True)
 
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
 
    def __repr__(self):
        return '<Pickups %d>' % self.id


class Trucks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Truck_number = db.Column(db.Integer,index=True)
    latitude = db.Column(db.Float(asdecimal=True),index=True)
    longitude = db.Column(db.Float(asdecimal=True),index=True)
 
    def __init__(self, Truck_number, latitude, longitude):
        self.Truck_number = Truck_number
        self.latitude = latitude
        self.longitude = longitude
 
    def __repr__(self):
        return '<Trucks %d>' % self.id

