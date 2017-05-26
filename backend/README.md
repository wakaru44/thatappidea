
# This App™ - This API

The backend for This App™.

A very simple backend that returns a simple playlist

TODO: Update this shit once we have a nice data store

# Endpoints

TODO: create the documentation and all this shit with swagger bitch

## hostname/v1/get_party?pid=XXXX

Retrieve the party for the given id.
Returns a json with the list of videos. Element 0 is the one currently playing.

## hostname/v1/add_vid?pid=XXXX&v=YYYY

Add the video YYYY to the party XXXX.
It returns the playlist too, with the video appended at the end.
