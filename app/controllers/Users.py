from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        # self.db = self._app.db
   
    def index(self):
        
        return self.load_view('index.html')

    def home(self):
        return self.load_view('home.html')

    def event(self):
        return self.load_view('event.html')

    def favorites(self):
        return self.load_view('favorites.html')

    def profile(self):
        return self.load_view('profile.html')