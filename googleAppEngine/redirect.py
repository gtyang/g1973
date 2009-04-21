
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

redirectMap = {
"/characterIssue.html":"http://www.makenotes.net/?p=1001",
"/DevNotes.html":"http://www.makenotes.net/?p=3"
}

class Redirector(webapp.RequestHandler):
    def get(self):
        self.redirect(redirectMap[self.request.path])
        self.response.set_status(301)

application = webapp.WSGIApplication(
                                     [('/.*', Redirector)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
