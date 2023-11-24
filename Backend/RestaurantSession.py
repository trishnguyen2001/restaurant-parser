
from werkzeug.datastructures import CallbackDict
from flask.sessions import SessionInterface, SessionMixin
from uuid import uuid4
from Restaurant import Restaurant, Dish
import json

class RestaurantSession(CallbackDict, SessionMixin):
    def __init__(self, initial=None, sid=None, new=False, restaurant=None):
        def on_update(self):
            self.modified=True
        CallbackDict.__init__(self, initial, on_update)
        self.restaurant = restaurant
        self.sid = sid
        self.new = new
        self.modified = False

class RestaurantSessionInterface(SessionInterface):
    session_class = RestaurantSession

    def __init__(self, restaurant=None):
        self.restaurant = restaurant

    def generate_sid(self):
        return str(uuid4())

    def open_session(self, app, request):
        # query cookie for sid
        sid = request.cookies.get(app.session_cookie_name)

        # open new session
        if (not sid) or (self.restaurant is None):
            print("[RestaurantSession.py] open_session(): NEW SESSION")
            if not sid:
                print("[RestaurantSession.py] open_session(): no SID")
                sid = self.generate_sid()
            if self.restaurant is None:
                print("[RestaurantSession.py] open_session(): no restaurant")
                self.restaurant = Restaurant()
            print("[RestaurantSession.py] open_session(): restaurant = ", self.restaurant, "\n$", self.restaurant.balance, ", ingrList: ", self.restaurant.ingredient_inventory, ", dishList: ", self.restaurant.dish_inventory)
            rSession = self.session_class(sid=sid, new=True, restaurant=self.restaurant)
            print("[RestaurantSession.py] open_session(): rSession restaurant = ", rSession.restaurant)
            return rSession
        
        # open existing session
        print("[RestaurantSession.py] open_session(): EXISTING SESSION ")
        balance = request.cookies.get('balance')
        ingrList = json.loads(request.cookies.get('ingrList'))
        dishList = json.loads(request.cookies.get('dishList'))
        r = Restaurant()
        r.setBalance(balance)
        r.setIngrList(ingrList)
        r.setDishList(dishList)
        print("[RestaurantSession.py] open_session(): restaurant = ", r)
        return self.session_class(initial=r, sid=sid)
     
    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        if not session:
            session.restaurant = None
            if session.modified:
                response.delete_cookie(app.session_cookie_name, domain=domain)
            return
        cookie_exp = self.get_expiration_time(app, session)
        response.set_cookie(app.session_cookie_name, session.sid, expires=cookie_exp, httponly=True, domain=domain) 
        response.set_cookie('balance', str(session.restaurant.balance), expires=cookie_exp, httponly=True, domain=domain) 
        response.set_cookie('ingrList', json.dumps(session.restaurant.ingredient_inventory),expires=cookie_exp, httponly=True, domain=domain) 
        response.set_cookie('dishList', json.dumps(session.restaurant.dish_inventory),expires=cookie_exp, httponly=True, domain=domain) 

    