from system.core.router import routes


routes['default_controller'] = 'Users'
routes['/home'] = 'Users#home'
routes['/event'] = 'Users#event'
routes['/favorites'] = 'Users#favorites'
routes['/concert-mapper'] = 'Users#concertmapper'
routes['/profile'] = 'Users#profile'
routes['POST']['/search-results'] = 'Users#search'
routes['/add-favorite'] = 'Users#add'

