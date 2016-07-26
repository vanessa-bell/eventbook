from system.core.router import routes


routes['default_controller'] = 'Users'
routes['/home'] = 'Users#home'
routes['/event'] = 'Users#event'
routes['/favorites'] = 'Users#favorites'
routes['/profile'] = 'Users#profile'
