from tornado.options import define, options


def load_options(config_file):

    # Blog options
    define('name', type=str, group='application', help='Name of the application.')
    define("description", type=str, group='application', help='Description of the application.')
    define("initial_balance", type=int, group='application', help='Initial account balance.')

    # General application settings
    define('port', type=int, group='application', help='Port to run the application from.')
    define('compress_response', type=bool, group='application', help='Whether or not to compress the response.')

    # Security options
    define('serve_https', type=bool, group='application', help='Whether to serve the application via HTTPS or not.')

    options.parse_config_file(config_file)
    base_options = options.group_dict('application')

    return base_options
