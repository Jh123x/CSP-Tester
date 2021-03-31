# Import libraries
import configparser
from os.path import exists
from flask import Flask, redirect


# Constants
CSP = None
CONFIG_FILE = './config.cfg'
OPTION_ERROR_MSG = 'Invalid option in %s option. It should be a %s value'

# Flask Application
app = Flask(__name__)


# Web app methods
@app.route('/<path:path>')
def redirect_to_main(path: str):
    """Redirect other URL to the main page"""
    return redirect('/')


@app.route('/')
def index():
    """Home page of the application"""
    with open('index.html') as file:
        return file.read()


@app.route('/script.js')
def script():
    """Load the javascript to the file"""
    with open('script.js') as file:
        return file.read()


@app.after_request
def load_csp(response, csp: str = CSP):
    """Load the global CSP"""
    response.headers['Content-Security-Policy'] = csp
    return response


# Config methods
def unpack_values(section: configparser.SectionProxy):
    """Unpack the values in the config parser"""

    # Get the values in settings
    csp = section.get('csp')
    host = section.get('host')
    debug = section.getboolean('debug')

    # Check for HTTPS option
    try:
        https = section.getboolean('https')
    except:
        raise configparser.NoOptionError(
            OPTION_ERROR_MSG % ('https', 'boolean (true/false)'))

    # Port option
    try:
        port = section.getint('port')
        if port > 65535 or port < 1:
            raise ValueError('Invalid port number')
    except:
        raise configparser.NoOptionError(section, OPTION_ERROR_MSG % (
            'port', 'Please use a value between 1 and 65535'))

    # Return the unpacked value
    return host, port, https, csp, debug


def generate_config():
    """Generate a default configuration"""
    parser = configparser.ConfigParser()
    parser['DEFAULT'] = {
        'http': False,
        'host': 'localhost',
        'port': 3000,
        'debug': False,
        'csp': 'default-src: *',
    }
    with open("config.cfg", "w") as file:
        parser.write(file)


if __name__ == "__main__":

    # If the configuration is not found
    if not exists('config.cfg'):
        generate_config()

    # Load the config
    parser = configparser.ConfigParser()
    parser.read(CONFIG_FILE)
    section = parser['DEFAULT']

    # Unpack the values
    HOST, PORT, HTTPS_BOOL, CSP, DEBUG = unpack_values(section)

    # Run the flask application
    app.run(HOST, PORT, ssl_context=HTTPS_BOOL, debug=DEBUG)
