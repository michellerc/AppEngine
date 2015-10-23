import jethro.page
import jethro.models
import webapp2
from webapp2_extras import jinja2


class Base(webapp2.RequestHandler):
    # make sure a webapp2 singleton is returned for caching
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    # wrapper to render jinja2 template, handles exception
    def render_template(self, template_name, template_values={}):
        template_values['_IS_DEBUG'] = self.app.debug
        template_file_name = "%s.html" % template_name
        self.response.out.write(self.jinja2.render_template(template_file_name, **template_values))

class MainHandler(Base):
    def get(self):
        self.render_template("form")

    def post(self):
        comment_store = jethro.models.Artist(name=self.request.POST['band'])
        comment_store.put()
        
class RootPageHandler(jethro.page.Base):

  def get(self):
    artists = jethro.models.Artist.query()
    self.render_template("index", {
            "artists": artists
            })
    
  def post(self):
    self.render_template("post_template", {
        })

class AlbumPageHandler(jethro.page.MainHandler):

  def get(self):
    self.render_template("albums", {
        "artist_id": self.request.get("artist_id")
        })

class ArtistPageHandler(webapp2.RequestHandler):
  def post(self):
    artist_name = self.request.get('artist_name')
    m = Music()
    m.artist = artist_name
    m.put()
    title = "Artist page"
    template_vars = {
    'title' : title
    }
    template = JINJA_ENVIRONMENT.get_template('artist.html')
    self.response.out.write(template.render(template_vars))

class SongPageHandler(webapp2.RequestHandler):
  def post(self):
    song_name = self.request.get('song_name')
    m = Music()
    m.song = song_name
    m.put()
    title = "Song page"
    template_vars = {
    'title' : title
    }
    template = JINJA_ENVIRONMENT.get_template('song.html')
    self.response.out.write(template.render(template_vars))
