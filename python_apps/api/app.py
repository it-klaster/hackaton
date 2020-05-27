from python_apps.api import create_app

app = create_app()
c = app.config

app.logger.info('>>>>> Starting development server at http://{}/<<<<<'.format(c['FLASK_SERVER_NAME']))

if __name__ == "__main__":
    app.run(debug=c['DEBUG'], host='0.0.0.0', port=c['PORT'])
