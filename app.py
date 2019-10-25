from config.environment import environment
from config.server import application


@application.errorhandler(404)
def page_not_found(e):
    return 'Undefined route', 404


if __name__ == '__main__':
    application.run(
        debug=environment['debug'],
        port=environment['port']
    )
