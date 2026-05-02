import pickle
import json


def add_music_band(data:list[dict], band:str):
    band = {"band": band, "album":[]}
    data.append(band)

def add_music_album(data:list[dict], album:str, band:str):

    for item in data:
        if item["band"] == band:
            item["album"].append(album)
            print(f"Added album {album} to band {band}")
            return

    print(f"{band} is not found")

def save_music_json(data:list[dict], filename:str="music.json"):
    with open(filename, 'w') as file:
        json.dump(data, file)

def save_music_pickle(data:list[dict], filename:str="music.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(data, file)

def load_music_json():
    with open("music.json", "r") as file:
        return json.load(file)

def load_music_pickle():
    with open("music.pkl", "rb") as file:
        return pickle.load(file)


music_data = []

add_music_band(music_data, "Metallica")
add_music_album(music_data, "Master of Puppets", "Metallica")

save_music_json(music_data)
save_music_pickle(music_data)

json_data = load_music_json()
pkl_data = load_music_pickle()

print(json_data)
print(pkl_data)
