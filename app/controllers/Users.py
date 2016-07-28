from system.core.controller import *
import json

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

    def add(self):
        print "hit add route"
        #need to add event data to db here...basically jData[x]['id'], jData[x]['title'], jData[x]['artists'][0]['image_url'],{{jData[x]['formatted_datetime']}},jData[x]['ticket_url']
        return redirect('/favorites')

    def profile(self):
        return self.load_view('profile.html')

    def concertmapper(self):
        return self.load_view('concert-mapper.html')

    def search(self,methods="POST"):
        artist= request.form['artist']
        location = request.form['location']
        radius = request.form['radius']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        print "successful form submission"
        url2 = 'http://api.bandsintown.com/artists/' + artist + '/events/recommended?location=' + location + '&date=' +start_date+','+end_date+'&radius=' + radius + '&app_id=eventbook&api_version=2.0&format=json'
        r = requests.get(url2)
        
        jData = json.loads(r.content)
        length = len(jData)
        
        
        if not jData:
            flash('Sorry, there are no results for that artist with your criteria. Please try again!','error')
            return redirect('/concert-mapper')
        else:       
            results = []
            for i in range(0,length):
                obj = []
                title = jData[i]['title']
                lat = float(jData[i]['venue']['latitude'])
                lng = float(jData[i]['venue']['longitude'])
                obj.append(title)
                obj.append(lat)
                obj.append(lng)
                results.append(obj)
               
            print results
        return self.load_view('success.html',jData=jData, lat=lat,lng=lng, artist=artist, length=length,results=results)



