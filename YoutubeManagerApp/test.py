import json

database_file_path = 'youtube.txt'

def load_data():
    with open(database_file_path,"r") as file:
        return json.load(file)


if __name__ == "__main__":
    videos = load_data() # list of dictionary hishab e nisi
    
    for video_file in videos: # each video_file in videos is a dictionary
        print(f"video name = {video_file['name']}, video duration = {video_file['time']}")
    
    # video_list = enumerate(videos,start=1)
    for item, video in videos:
        print(f"{item}, {video}")