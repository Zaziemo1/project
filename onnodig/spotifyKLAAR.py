import requests

# data die je haalt uit de instellingen van je api op de site van spotify dit heb je nodig
data = {
    'grant_type': 'client_credentials',
    'client_id': '4cc048fb419440f5951860cf0a9f9db0',
    'client_secret': '763a491995ce4b1cad73ecccd6bb9ade',
}

# acces token
response_json = requests.post(
    'https://accounts.spotify.com/api/token', data=data).json()
access_token = response_json["access_token"]

# headers
headers = {
    'Authorization': f'Bearer {access_token}',
}



while True:

    keuze_gebruiker = int(input("""kies een optie: 
    1: Top-Tracks
    2: Albums van een bepaalde artiest
    3: artiest van een Album zoeken
    4: STOP
                : """))

    if keuze_gebruiker == 1:

        artist_name = input("type an artist: ")
        # krijg de gegevens van de artist
        get_artist = requests.get(
            f'https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1', headers=headers).json()["artists"]["items"]

        # als je waarde 0 is dan print geen artiest gevonden
        if len(get_artist) == 0:
            print("no artist found with this name")
            continue

        # top tracks van de artiest
        top_tracks = requests.get(
            f'https://api.spotify.com/v1/artists/{get_artist[0]["id"]}/top-tracks?country=US', headers=headers).json()["tracks"]

        for index, track in enumerate(top_tracks):
            # print de namen van de top tracks
            print(f'{index + 1}: {track["name"]}')

        related_artist = input("gerelateerden artiesten bekijken? ja of nee: ")

        if related_artist == "nee":
            continue

        if related_artist == "ja":
            # gerelateerde artiest endpoint
            related_artists = requests.get(
                f'https://api.spotify.com/v1/artists/{get_artist[0]["id"]}/related-artists', headers=headers).json()["artists"][0]["name"]  # [artists][0][name]de naam van de artiest

            print(related_artists)

        # id van de gerelateerde artist zodat we later in de code de top tracks kunnen krijgen van deze artiest
        related_artists_id = requests.get(
            f'https://api.spotify.com/v1/artists/{get_artist[0]["id"]}/related-artists', headers=headers).json()["artists"][0]["id"]

        toptracks_relatedartist = input(
            "wil je de top tracks van deze artist ook weten? Ja of nee: ")

        if toptracks_relatedartist == "nee":
            continue

        # als ja dan ...
        if toptracks_relatedartist == "ja":

            # top tracks van de gerelateerde artiest
            top_tracks_related_artist = requests.get(
                f'https://api.spotify.com/v1/artists/{related_artists_id}/top-tracks?country=US', headers=headers).json()["tracks"]

            for index, track in enumerate(top_tracks_related_artist):
                print(f'{index + 1}: {track["name"]}')

    if keuze_gebruiker == 2:

        artist_name = input("type an artist: ")

        # krijg de artiest gegevens
        get_artist = requests.get(
            f'https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1', headers=headers).json()["artists"]["items"]

        # als je waarde 0 is dan print geen artiest gevonden
        if len(get_artist) == 0:
            print("no artist found with this name")
            continue

        # krijg albums van de artiest
        albums = requests.get(
            f'https://api.spotify.com/v1/artists/{get_artist[0]["id"]}/albums?&country=US&limit=10', headers=headers).json()["items"]

        for album in albums:  # for loop om alle albums eruit te halen
            print(f'- {album["name"]}')

    if keuze_gebruiker == 3:

        album_name = input("typ een album naam: ")

        # krijg de album gegevens/zoek naar de album endpoint
        get_album = requests.get(
            f'https://api.spotify.com/v1/search?q={album_name}&type=album&limit=1', headers=headers).json()["albums"]["items"]

        # print de naam van de artiest
        print(f'name artist: {get_album[0]["artists"][0]["name"]}')

        album_track = input("wil je tracks van deze album? ja of nee: ")

        if album_track == "nee":
            continue

        if album_track == "ja":

            # tracks van de album endpoint
            get_album_tracks = requests.get(
                f'https://api.spotify.com/v1/albums/{get_album[0]["id"]}/tracks?offset=0&limit=20', headers=headers).json()["items"]

            for track in get_album_tracks:  # print alle tracks onder elkaar
                track["name"]
                print(f"    - {track['name']}")

    # if 4 dan stop
    if keuze_gebruiker == 4:
        break
