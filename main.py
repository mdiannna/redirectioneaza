
import webapp2

from appengine_config import SESSION_SECRET_KEY

from webapp2_extras import routes
from webapp2 import Route as r

# the public part of the app
from controllers.site import *
from controllers.account import *

from controllers.ngo import NgoHandler, TwoPercentHandler, TwoPercent2Handler, DonationSucces


config = {
    'webapp2_extras.auth': {
        'user_model': 'models.user.User',
        'user_attributes': ['name']
    },
    # by default the session backend is the cookie
    # cookie_name: session
    # session_max_age: None => until the client is closed
    'webapp2_extras.sessions': {
        'secret_key': SESSION_SECRET_KEY
    }
}

app = webapp2.WSGIApplication([
        r('/',          handler=HomePage),

        r('/despre',    handler=AboutHandler),
        # r('/cont-nou',  handler=NewAccountHandler),
        r('/signup',    handler=SignupHandler),
        r('/login',     handler=LoginHandler, name='login'),
        r('/logout',    handler=LogoutHandler, name='logout'),

        r('/forgot',    handler=ForgotPasswordHandler, name='forgot'),
        r('/password',  handler=SetPasswordHandler),
        r('/<type:v|p>/<user_id:\d+>-<signup_token:.+>', handler=VerificationHandler, name='verification'),

        r('/<ngo_url>', handler=NgoHandler),
        r('/catre/<ngo_url>', handler=NgoHandler),

        r('/<ngo_url>/doilasuta',           handler=TwoPercentHandler),
        r('/<ngo_url>/doilasuta/pas-2',     handler=TwoPercent2Handler),
        r('/<ngo_url>/doilasuta/succes',    handler=DonationSucces),


        # r('/contul-meu', handler=MyAccountHandler, name='contul-meu')
    ],
    debug=True,
    config=config
)
