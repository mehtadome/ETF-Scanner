#!/bin/bash
CLIENT_ID=
CLIENT_SECRET=

echo "Attempting Access Token cURL"
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}"

# Author's Note: This file is for running cURL commands through a terminal. 
#    You shouldn't need the access token when using spotipy.