from system.core.router import routes


routes['default_controller'] = 'Users'
routes['/home'] = 'Users#home'
routes['POST']['/register'] = 'Users#register'
routes['/event'] = 'Users#event'
routes['/favorites'] = 'Users#favorites'
routes['/discover'] = 'Users#discover'
routes['/profile'] = 'Users#profile'
routes['POST']['/search-results'] = 'Users#search'
routes['POST']['/update-location'] = 'Users#updatelocation'
routes['/add-favorite'] = 'Users#add'

