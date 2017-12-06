import json
from flask import request, jsonify, Blueprint, abort, render_template, flash, redirect,url_for
from flask.views import MethodView
from my_app import db, app
from my_app.catalog.models import Trucks,Pickups
from .forms import LoginForm

catalog = Blueprint('catalog', __name__)
 

@catalog.route('/message')
def message():
    return render_template('add.html')


@catalog.route('/',methods=['GET', 'POST'])
@catalog.route('/home',methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    error = None
    if request.method == 'POST':
        if form.validate():
            truck = Trucks(form.Truck_number.data, str(form.latitude.data),str(form.longitude.data))
            db.session.add(truck)
            db.session.commit()
            flash('You were successfully logged in')
            return redirect(url_for('catalog.message'))

        else:
            error = 'Check the entered values'
    return render_template('index.html', 
                           title='add',
                           form=form ,error = error)
 
 
class TrucksView(MethodView):
 
    def get(self, tno=None, page=1):
        if not tno:
            trucks = Trucks.query.paginate(page, 10).items
            res = {}
            for truck in trucks:
                res[truck.id] = {
                    'Truck_number': truck.Truck_number,
                    'latitude': str(truck.latitude),
                    'longitude': str(truck.longitude),
                }
        else:
            truck = Trucks.query.filter_by(Truck_number=tno).first()
            if not truck:
                abort(404)
            res = {
                    'Truck_number': truck.Truck_number,
                    'latitude': str(truck.latitude),
                    'longitude': str(truck.longitude),            }
        return jsonify(res)
 
    def post(self):
        Truck_number = request.form.get('Truck_number')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        truck = Trucks(Truck_number, latitude, longitude )
        db.session.add(truck)
        db.session.commit()
        return jsonify({truck.id: {
                    'Truck_number': truck.Truck_number,
                    'latitude': str(truck.latitude),
                    'longitude': str(truck.longitude),
        }})


Trucks_view =  TrucksView.as_view('Trucks_view')
app.add_url_rule(
    '/trucks/', view_func=Trucks_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/trucks/<int:tno>', view_func=Trucks_view, methods=['GET']
)
app.add_url_rule(
    '/trucks/page/<int:page>', view_func=Trucks_view,  methods=['GET']
)


class PickupsView(MethodView):

    def get(self, tno=None, page=1):
        if not tno:
            pickups = Pickups.query.paginate(page, 10).items
            res = {}
            for pickup in pickups:
                res[pickup.id] = {
                    'latitude': str(pickup.latitude),
                    'longitude': str(pickup.longitude),
                }
        return jsonify(res)
 
    def post(self):
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        pickup = Pickups( latitude, longitude )
        db.session.add(pickup)
        db.session.commit()
        return jsonify({pickup.id: {
                    'latitude': str(pickup.latitude),
                    'longitude': str(pickup.longitude),
        }})


 
Pickups_view =  PickupsView.as_view('Pickups_view')
app.add_url_rule(
    '/pickups/', view_func=Pickups_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/pickups/page/<int:page>', view_func=Pickups_view,  methods=['GET']
)
