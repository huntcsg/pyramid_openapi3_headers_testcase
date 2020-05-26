from pyramid.view import view_config
from pyramid.config import Configurator
from wsgiref.simple_server import make_server


@view_config(
    route_name='hello',
    openapi=True,
)
def hello(request):
    return {'message':'hello'}


def main():
    with Configurator() as config:
        config.include("pyramid_openapi3")
        config.pyramid_openapi3_spec('openapi.yaml', route="/opesnapi.yaml")
        config.pyramid_openapi3_add_explorer(route="/swagger")
        config.add_route('hello', '/hello')

        config.scan()

        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()

if __name__ == '__main__':
    main()
