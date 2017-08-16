# server.py
import datetime
import sys

import falcon

import image_processing

logfile = "logfile.txt"

def validate_token(req, resp):
    try:
        token = req.get_param('token')

    except:
        resp.status = falcon.HTTP_401
        resp.body = "Error: 401 \n there appears to be a problem with your request"

# Receipts
@falcon.before(validate_token)
class ReceiptData(object):
    def on_get(self, req, resp):

        try:
            # decrypt JWT token with JWE
            token = req.get_param('token')
            resp.status = falcon.HTTP_200
        except:
            problem = "{} - {}: class ReceiptData() Exception: {}".format(
                    datetime.datetime.now().date(),
                    datetime.datetime.now().time(),
                    sys.exc_info()[0])
            with open(logfile, 'a') as file:
                file.write(problem)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_FORBIDDEN

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_FORBIDDEN

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_FORBIDDEN

@falcon.before(validate_token)
class ReceiptImage(object):
    def on_get(self, req, resp):
        token = req.get_param('token')

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_FORBIDDEN

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_FORBIDDEN

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_FORBIDDEN


# Users
@falcon.before(validate_token)
class UserName(object):
    def on_get(self, req, resp):
        token = req.get_param('token')

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_FORBIDDEN

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_FORBIDDEN

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_FORBIDDEN

class AuthorizeUser(object):
    def on_get(self, req, resp):
        token = req.get_param('token')

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_FORBIDDEN

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_FORBIDDEN

    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_FORBIDDEN
