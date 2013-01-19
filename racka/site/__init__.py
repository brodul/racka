def includeme(config):
    config.add_static_view('static', 'racka.site:static')
    config.add_jinja2_search_path("racka.site:templates")
    config.add_route('home', '/')
    config.scan('.')
