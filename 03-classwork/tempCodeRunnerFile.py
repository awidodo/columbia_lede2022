print(spotify_data.keys())

print(spotify_data['artists'].keys())

#square brackets make it a list, 0 to get the first item
print(spotify_data['artists']['items'][0].keys())

#print name out
print(spotify_data['artists']['items'][9]['name'])
