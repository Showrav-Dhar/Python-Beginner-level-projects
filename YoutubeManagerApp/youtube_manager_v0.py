import json

video_database_file = 'youtube.txt'

def load_data():
    try:
        with open(video_database_file,'r') as file:
            return json.load(file) # loads the json file as list of dictionaries
    except FileNotFoundError:
        return [] # returns empty list

def save_data_helper(videos):
    ## saves videos in the json file
    with open(video_database_file,'w') as file:
        json.dump(videos, file) # json dump method

def list_all_videos(videos):
    video_list = enumerate(videos,start=1)

    print('List of currently stored videos\n')
    print('*'*50)
    
    for index, video in video_list:
        
        print(f"{index}. Video Name = {video['name']}, Duration = {video['time']}") # as the add video method is storing like this format
    
    print('\n')
    print('*'*50)
    
    
def add_video(videos):
    # this method gets input the whole -> videos database as json format
    # user will be asked which video to add inside this function

    video_name = input("Enter video name : ")
    video_time = input("Enter video length : ")
    
    videos.append({'name':video_name,'time':video_time}) # video will be stored as {'name':iron_man, 'time':20min} as the json format
    # video is added as a dictionary,one video is added is one dictionary
    print("---Video added sucessfully---")
    save_data_helper(videos)
    

def update_video(videos):
    # this method will take all the videos as parameter
    # use will have the option to update the video information in this method
    print("--- Which video do you want to update? ---")
    list_all_videos(videos)
    video_index = int(input("Enter video number to update : "))
    
    if 1 <= video_index <= len(videos):
        new_video_name = input("Enter the new video name : ")
        new_video_time = input("Enter new video time : ")
        
        videos[video_index-1] = {'name':new_video_name, 'time' : new_video_time} # video_index - 1, because original index starts from 0
        
        print("---Video updated sucessfully---")
        save_data_helper(videos)
    else:
        print("Invalid index selected")
    
def delete_video(videos):
    
    print("--- Which video do you want to delete? ---")
    list_all_videos(videos)
    video_index = int(input("Enter video number to be deleted : "))
    
    if 1 <= video_index <= len(videos):
        del videos[video_index-1]
        
        print("---Video deleted sucessfully---")
        save_data_helper(videos)
    else:
        print("Invalid index selected")
    

# starting of the program in command line

def main():
    videos = load_data() # goes into a file and then loads, will be loaded as json file format

    while True:
        print('\n Welcome to the Youtube Manager || choose an input')
        print('1. List of favourite videos')
        print('2. Add a youtube video')
        print('3. Update the youtube video detail')
        print('4. Delete a youtube video')
        print('5. Exit the program')
        choice = input("Enter your choice : ")
        # print(videos)

        match choice: # in every method we are passing the whole database
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video (videos)
            case '4':
                delete_video (videos)
            case '5':
                # exits the app
                print("Thank you!")
                break
            case _: ### handles all other input rather than 1 to 5
                print("Invalid choice")


if __name__ == "__main__":
    main()