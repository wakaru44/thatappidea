# -*- coding: utf-8 -*-

from thisapi import app

if __name__ == '__main__':
    if not app.debug:
        import logging
        from logging.handlers import TimedRotatingFileHandler
        file_handler = TimedRotatingFileHandler(
            "myapp.log",
            when="D",
            backupCount=10
            )
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Is it here?
    app.debug = app.config['DEBUG']
    app.run(host="0.0.0.0")
