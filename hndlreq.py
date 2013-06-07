import webapp2
import random

from frtn import *

def getfrtncookie():
	return fortunes[random.randint(1,len(fortunes))][0].strip()

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write("Confucius say "+getfrtncookie())
		self.response.write(" And, you are awesome! ")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

