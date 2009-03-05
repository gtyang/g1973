# coding: gbk
import logging
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
    for g in greetings:
        g.content = g.content.encode('GBK')

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
    path = os.path.join(os.path.dirname(__file__), 'guestbook.template')
    self.response.out.write(template.render(path, template_values))
	
class Guestbook(webapp.RequestHandler):
  def post(self):
    greeting = Greeting()

    self.request.charset = "GBK"
    if users.get_current_user():
      greeting.author = users.get_current_user()

    greeting.content = cgi.escape(self.request.get('content'))
    greeting.put()
    self.redirect('/guestbook')

class ZhugeChengming(webapp.RequestHandler):
  def get(self):
    y = self.request.get('y')
    m = self.request.get('m')
    d = self.request.get('d')
    ny = self.request.get('ny')
    nm = self.request.get('nm')
    nd = self.request.get('nd')
    t = self.request.get('t')
    if ny.isdigit() and nm.isdigit() and nd.isdigit() and t.isdigit():
      rslt = chengMing(ny,nm,nd,t)

      template_values = {
       'weight':rslt[0],
       'shi':rslt[1],
	   'y':y,
	   'm':m,
	   'd':d,
       'ny':ny,
	   'nm':nm,
	   'nd':nd,
	   't':t
       }
    else:
      template_values = {
       'weight':'',
       'shi':'囧，我算不出您的命....ORZ',
	   'y':y,
	   'm':m,
	   'd':d,
       'ny':ny,
	   'nm':nm,
	   'nd':nd,
       't':t
       }

    path = os.path.join(os.path.dirname(__file__), 'zhugechengming/chengming.template')
    self.response.headers['Content-Type'] = 'text/html;charset=GBK'
    self.response.out.write(template.render(path, template_values))
	
	
class JsonProcessor(webapp.RequestHandler):
    def get(self):
        y = self.request.get('y')
        m = self.request.get('m')
        d = self.request.get('d')
        t = self.request.get('t')

        if y.isdigit() and m.isdigit() and d.isdigit() and t.isdigit():
            rslt = chengMing(y,m,d,t)
        else:
            rslt = [-1,"Input error!"]

        self.response.headers['Content-Type'] = 'application/json;charset=utf-8'
        # self.response.headers['Content-Type'] = 'text/plain;charset=utf-8'
        self.response.out.write('{\n')
        self.response.out.write('"weight":"' + str(rslt[0]) + '",\n')
        self.response.out.write('"poem":"' + unicode(rslt[1],"gbk") + '"\n')
        self.response.out.write('}')

application = webapp.WSGIApplication(
                                     [('/guestbook', MainPage),
                                      ('/sign', Guestbook),
									  ('/zhugechengming/cheng',ZhugeChengming),
                                      ('/jsonprocessor',JsonProcessor)],
                                     debug=True)
									 
def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
