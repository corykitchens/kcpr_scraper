from selenium import webdriver
from bs4 import BeautifulSoup



class ChromeOptions(webdriver.ChromeOptions):
  def __init__(self, args=[]):
    super(ChromeOptions, self).__init__()
    for arg in args:
      self.add_argument(arg)

class HeadlessBrowser(webdriver.Chrome):
  def __init__(self, args=[]):
    try:
      super(HeadlessBrowser, self).__init__(options=ChromeOptions(args))
    except Exception as e:
      raise e

def scrape_kcpr():
  url = "http://kcpr.org/list"
  headless_browser = HeadlessBrowser(['--headless', '--no-sandbox', '--disable-dev-shm-usage'])
  headless_browser.get(url)
  html = headless_browser.page_source
  soup = BeautifulSoup(html, 'html.parser')
  tracks = []
  # Traversing/Extracting 
  recent_songs = soup.find_all('div', {'class': 'recentsong'})
  for song in recent_songs:
    song_title = song.find('span', {'class': 'songpart'})
    song_title = song_title.b.string
    artist = song.find('span', {'class': 'artistpart'})
    artist = artist.b.string
    album = song.find('span', {'class': 'diskpart'})
    print(album)
    # album = album.b.string
    tracks.append({'artist': artist, 'song_title': song_title, 'album': album})
  print(tracks)

if __name__=="__main__":
  scrape_kcpr()
