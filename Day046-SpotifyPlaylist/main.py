import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()
date = input("Enter Date in format of YYYY-MM-DD: ")
# date="2000-08-12"
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")

songs_url = response.text
# uri_redirect = 'http://localhost:8888/callback'
# authorize_endpoint = 'https://api.spotify.com/authorize'
# request_authorization_parameters = {'client_id': 'here I give my client id',
#                                                                    'response_type': 'code',
#                                                                    'redirect_uri': uri_redirect,
#                                                                     'scope': 'user-library-read playlist-read-private'}
# r_auth = requests.get(authorize_endpoint, params=request_authorization_parameters)

soup = BeautifulSoup(songs_url,"html.parser")
div_selector = soup.find_all(name="div",class_="o-chart-results-list-row-container")

list_title = [each.find(name="li", class_="lrv-u-width-100p").find(name="h3",id="title-of-a-story", class_="c-title").getText() for each in div_selector]
list_title=[title.replace("\n","").replace("\t","") for title in list_title]

print(list_title)

# auth_manager = SpotifyClientCredentials(auth_manager=SpotifyClientCredentials(client_id=os.environ["SPOTIFY_ID"],client_secret=os.environ["SPOTIFY_SECRET"]))
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["SPOTIFY_ID"],client_secret=os.environ["SPOTIFY_SECRET"],redirect_uri="http://localhost:8888/callback",scope="playlist-modify-private"))
user_id = sp.current_user()["id"]
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
# sp.user_playlist_create(user=os.environ["SPOTIFY_ID"], name=f"{date} Top 100 Songs", public=True, collaborative=False, description=f"This playlist is created by python bot for the date of {date}")
# user_id = sp.current_user()["id"]
url = f"https://api.spotify.com/v1/me/"
parameter = {"access_token": "BQBKpU-jHl26g9j_1sLlR5HJ4WdBc6JDGVz_twg8rKLe3Lv5BR8Q6xaGku_vtdpGdWOGKYGgkCI_unslQlMhypOSQaznPGoUpCXy0fyFGSRas_fg9gEceWz-wvUS9ttFd_owlwzkfm_Hb7RyGIJBciJssqzlsiCT_h6w6QEaT0crKKrIh6XpkXcfzEJ4puUx70b1mpkwFTA18i2IPWuZd2keDmVOrEQeag", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "AQAyfQ3nSeSAuqUl0ISks8U1N9u3K7vlvefKwG2pWYNLt1TfK8z1pMB-OOtKpXcVEjlsyw_wR77474LLEsZs1mzhPexcGwGRrUkTX3hj1CGBPdiWWK3AmgGTi4769iTXFaY", "scope": "playlist-modify-private", "expires_at": 1704283458}
spotify_response = requests.get(url=url,params=parameter)

data=spotify_response.json()
print(data)
year = date.split("-")[0]
uri_list = []

for song in list_title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Top 100 Songs", public=False, collaborative=False, description=f"This playlist is created by python bot for the date of {date}")
# print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)