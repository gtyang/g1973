import os
from google.appengine.ext.webapp import template

import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

from zhugechengming.ChengMing import chengMing

class Greeting(db.Model):
  author = db.UserProperty()
  content = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
  def get(self):
    greetings_query = Greeting.all().order('-date')
    greetings = greetings_query.fetch(10)

    if users.get_current_user():
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Logout'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Login'

    template_values = {
      'greetings': greetings,
      'url': url,
      'url_linktext': url_linktext,
      }
    self.response.headers['Content-Type'] = 'text/html;charset=GBK'
    path = os.path.join(os.path.dirname(__file__), 'index.template')
    self.response.out.write(template.render(path, template_values))
	
class Guestbook(webapp.RequestHandler):
  def post(self):
    greeting = Greeting()

    if users.get_current_user():
      greeting.author = users.get_current_user()

    greeting.content = self.request.get('content')
    greeting.put()
    self.redirect('/guestbook')

class ZhugeChengming(webapp.RequestHandler):
  def get(self):
    y = self.request.get('y')
    m = self.request.get('m')
    d = self.request.get('d')
    t = self.request.get('t')
    if y.isdigit() and m.isdigit() and d.isdigit() and t.isdigit():
      rslt = chengMing(y,m,d,t)

      template_values = {
       'weight':rslt[0],
       'shi':rslt[1],
	   'y':y,
	   'm':m,
	   'd':d,
	   't':t
       }
    else:
      template_values = {
       'weight':'',
       'shi':'',
	   'y':y,
	   'm':m,
	   'd':d,
	   't':t
       }

    path = os.path.join(os.path.dirname(__file__), 'zhugechengming/chengming.template')
    self.response.headers['Content-Type'] = 'text/html;charset=GBK'
    self.response.out.write(template.render(path, template_values))
	
	
application = webapp.WSGIApplication(
                                     [('/guestbook', MainPage),
                                      ('/sign', Guestbook),
									  ('/zhugechengming/cheng',ZhugeChengming)],
                                     debug=True)
									 
def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
