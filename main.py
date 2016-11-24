#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

class PlusHandler(BaseHandler):
    def post(self):
        plus_1 = self.request.get("plus_1")
        plus_2= self.request.get("plus_2")
        rezultat_plus = int(plus_1) + int(plus_2)
        params = {"rezultat_plus": rezultat_plus}
        return self.render_template("plus.html", params=params)
        self.write(rezultat_plus)

class MinusHandler(BaseHandler):
    def post(self):

        minus_1= self.request.get("minus_1")
        minus_2 = self.request.get("minus_2")
        rezultat_minus = int(minus_1) - int(minus_2)
        params = {"rezultat_minus": rezultat_minus}
        return self.render_template("minus.html", params=params)
        self.write(rezultat_minus)

class DeljenjeHandler(BaseHandler):
    def post(self):

        deljenje_1= self.request.get("deljenje_1")
        deljenje_2 = self.request.get("deljenje_2")
        rezultat_deljenje = int(deljenje_1) / int(deljenje_2)
        params = {"rezultat_deljenje": rezultat_deljenje}
        return self.render_template("deljenje.html", params=params)
        self.write(rezultat_deljenje)

class MnozenjeHandler(BaseHandler):
    def post(self):

        mnozenje_1= self.request.get("mnozenje_1")
        mnozenje_2 = self.request.get("mnozenje_2")
        rezultat_mnozenja = int(mnozenje_1) * int(mnozenje_2)
        params = {"rezultat_mnozenja": rezultat_mnozenja}
        return self.render_template("mnozenje.html", params=params)
        self.write(rezultat_mnozenja)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/minus', MinusHandler),
    webapp2.Route('/plus', PlusHandler),
    webapp2.Route('/deljenje', DeljenjeHandler),
    webapp2.Route('/mnozenje', MnozenjeHandler)
], debug=True)
