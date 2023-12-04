import json
import requests
from PIL import Image
filename =  'geschiedenis.json' #bestandsnaam 
geschiedenis = {} #maakt een lege dictionary aan

with open(filename, "r") as f: #opent de bestand genaamd geschiedenis.json als f
    geschiedenis = json.load(f)  #slaat alles van f in de lege dictionary




keuze = 0 
while keuze != 4:
  while True:
    keuze = int(input("""What do you want to search:
        1-Album
        2-Artist
        3-Track
        4-Stop 
        5-Geschiedenis
                """)) #vraagt de gebruiker wat hij wil opzoeken

    if keuze == 1:
        album = str(input("Name an album:   ")) #vraagt de gebruiker om de album naam
        url = f'https://api.deezer.com/search?q=album:"{album}"' #maakt de url met de album naam
        response = requests.get(url) #pakt alles van de url en zet dat in response
        response_json = response.json() #veranderd de response in een json file en zet dat in een nieuwe variabele response_json
        counter = 0 #counter is 0
        if response_json['total'] == 0: #als er geen liedjes zit in de album of als de albm niet bestaat
            print("This album doesnt have any song or doesnt exist!!")#print de album heeft geen liedjes of bestaat niet
            break #stopt meteen en begint opnieuw 
        print(f"This album has been made by {response_json['data'][0]['artist']['name']}") #print de artisten naam door in de dictionary naar zijn naam te gaan
        geschiedenis['album'].append(album) #voegt de album toe aan de dictionary als album

        while True: 
            counter = int(counter)
            print(response_json['data'][counter]['title'])#print elke songtitle van de album 
            counter = counter+1
            if counter >= len(response_json["data"]): #als counter groter is dan de aantal liedjes in de album
                break #stopt het met de while loop
        image2 = response_json['data'][0]['album']['cover_big'] #image2 is de url van de album cover
        im = Image.open(requests.get(image2, stream=True).raw) #im is alles van de url in im
        im.show() #opent im met de standaard windows programma
        keuze2 = input(
            f"Would you like to see more of {response_json['data'][0]['artist']['name']}? yes or no?   ") #vraagt de gebruiker of hij meer wilt zien
        if keuze2.upper() == 'YES': #als de gebruiker meer wilt zien

            url2 = f"https://api.deezer.com/artist/{response_json['data'][0]['artist']['id']}/albums" #url2 is gelijk aan de api url met de artisten id 
            response = requests.get(url2) #is alles van de url2 en zet dat in de variable response
            response_json = response.json() #response_json maakt van response een json file
            counter2 = 0 #counter2 is 0
            album = 1 #album is 1

            while True:
                print(
                    f"Album {album}: {response_json['data'][counter2]['title']}") #print de album nummer en de album title
                counter2 = counter2+1 #counter2 plus 1 
                album = album+1 #album plus 1

                if counter2 >= len(response_json["data"]): #als counter2 groter is dan de aantal albums 
                    break #dan stopt de while loop
        elif keuze2.upper() == 'NO': #als de gebruiker niet meer wilt zien
            break #break
        else: #als de gebruiker geen ja of nee zegt dan stopt die ook
            print("Answer with yes or no!!!")
            break

    if keuze == 2: #als keuze 2 is
        artist = str(input("Name a artist:    ")) #vraagt naaar een artist
        url = f'https://api.deezer.com/search?q=artist:"{artist}"' #maakt een url met de artisten naam
        response = requests.get(url) #haalt alles van de url en zet at weer in response
        response_json = response.json() #maakt van response een json file en zet dat in response_json
        if response_json['total'] == 0: #als de total 0 is dan heeft de artist geen liedjes of bestaat de artist niet
            print("This artist doesnt exist or doesnt have any songs!!")
            break #stopt de while loop
        geschiedenis['artist'].append(artist) #voegt de artist toe aan de dict geschiedenis
        print(f"""The most recent track: {response_json['data'][0]['title']}, its ranked {response_json['data'][0]['rank']} and its duration is {response_json['data'][0]['duration']}.
            The most recent album: {response_json['data'][0]['album']['title']},""") #print de meeste recente lied, de plaats op de ranglijst, de lengte van de lied en de meest recente album
        keuze3 = input("Do you want to see the artist?  ") #vraagt de gebruiker of hij de artist wilt zien
        if keuze3.upper() == 'YES': #als het antwoord ja is
            image = response_json['data'][0]['artist']['picture_big'] #image is de url met de foto van de artist
            im = Image.open(requests.get(image, stream=True).raw) #zet alles van de url in im 
            im.show() #laat de im zien met de standaar windows programma voor png en jpg
        elif keuze3.upper() == 'NO': #als het antwoord nee is
            break #stopt de while loop
        else: #als het geen nee of ja is 
            print("Answer with yes or no!!")
            break #stopt de while loop ook

    if keuze == 3:
        track = str(input("Name the track you want to seach:      ")).upper() #welke liedje wil je opzoeken
        artist = str(input("Which artist made the song:     ")).upper() #door welke artist is het gemaakt
        url = f'https://api.deezer.com/search?q=track:"{track}"' #maakt een url met de liedje
        response = requests.get(url) #haalt alles van de url en zet dat in response
        response_json = response.json() #maakt van response een json file
        if response_json['total'] == 0: #als totaal 0 is
            print("This track doesnt exist or hasnt been released yet!!!") #dan bestaat het liedjes niet of is het nog niet uitgebracht
            break #stopt de while loop
        geschiedenis['track'].append(track) #voegt de liedje toe aan de lege dict
        counter2 = 0 #counter2 is 0
        while True:
            counter2 = int(counter2) #maakt van counter 2 een integer

            if artist == response_json['data'][counter2]['artist']['name'].upper(): #als de naam van de artist gelijk is als de naam
                print(f"Made by {response_json['data'][counter2]['artist']['name']},{response_json['data'][counter2]['title']}. Its duration is {response_json['data'][counter2]['duration']}s and its ranked {response_json['data'][counter2]['rank']}") #dan print hij weer de naam van de liedje, de artist naam, de duration van het lied en de plaats op de ranglijst
                if response_json['data'][counter2]['explicit_lyrics'] == True: #als de explicit_lyrics true zijn dan zijn er scheldwoorden of woorden die niet zo netjes zijn
                    print("This track contains explicit lyrics!") #orint die dat er explicite lyrics bevat
                else: #en anders 
                    print("This track doesnt contain explicit lyrics!") #bevat het geen explicite lyrics
                break #stopt de while loop

            counter2 = counter2 + 1
    if keuze == 4: #als keuze 4 is 
        print("Goodbye!") #print die Doei en stopt de while loop ook
        
        with open(filename, "w", newline="") as fp: #opent die de json bestand geschiedenis.json als fp
            json.dump(geschiedenis,fp) #zet alles van de dict geschiedenis in de json bestand
        break #stopt de while loop
    if keuze == 5: #als keuze 5 is 
        print("Here is your history.") #dan laat hij jou de op dit momente geschiedenis zien
        print(geschiedenis) #print die de dict geschiedenis
    else: #en anders
        print("Please type a number between 1 and 5! ") #heeft de gebruiker geen cijfer tot en met 5 getypt en moet hij opnieuw beginnen
