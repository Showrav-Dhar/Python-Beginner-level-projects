import json

video_database_file = 'youtube.txt'

def load_data():
    try:
        with open(video_database_file,"r") as file:
            return json.load(file) 
        # the videos variable inside the main funciton will load the database as a list of dictionary, 
        # as, we are saving the video in that format, 
        # and the reason behind that is we want to save the information as json format
        
    except FileNotFoundError:
        return []

def save_data_helper(videos): ## updates the database
    # this basically writes the whole file again, with the new -> videos variable
    # as every time we make any changes to the videos variable, we basically
    # make changes to the list of dictionary which is callsed the videos variable,
    # after starting of the program we are loading the entire .txt file in the videos variable
    # and do our editing in that variable, as that is a list of dictionary at its core
    # so it is easy to perform update and delete operataion
    
    with open(video_database_file,'w') as file:
        json.dump(videos,file,indent=2)
    
def list_all_videos(videos): # method 1
    # videos - is list of dictionary
    
    video_list = enumerate(videos,start=1) # makes the list of dictionary a iteratable object
    
    print('List of currently stored videos\n')
    print("_"*100)
    
    for index, video_file in video_list: # video_file is a dictionary itself
        print(f"{index}. Video Name = {video_file['name']}, Video Duration = {video_file['time']}")
    
    print('\n')
    print("_"*100)
        
def add_video(videos): # method 2
    # the method is recieving a list of dictionaries
    
    video_name = input("Enter Video Name - ")
    video_time = input("Video Duration - ")
    
    # now adding these information, as a dictionary inside the list 
    videos.append({'name':video_name, 'time':video_time})
    print("---- Video has been added successfully ----")
    
    save_data_helper(videos) ## updates the database
    
    
def update_video(videos): # method 3
    # user will update the video information by selecing video number
    
    # so, what is happening is -> the method is taking the videos, which is a list of dictionary
    # then taking user input, which video number the user wants to edit
    
    
    print("--- Which video you want to update? || Select video number ---")
    list_all_videos(videos)
    video_index = int(input("Enter video index number - "))
    
    if 1 <= video_index <= len(videos):
        new_video_name = input("Enter name of the new video - ")
        new_video_length = input("Enter duration of the new video - ")
        
        # assiging a new dictionary at that position, so the old one gets removed anyway
        videos[video_index-1] = {'name':new_video_name, 'time': new_video_length}
        
        print("---- Video Updated Successfully ----")
        save_data_helper(videos) ## updates the database
        
        print(" --- Updated List ---")
        list_all_videos(videos)
    else:
        print("Invalid index selected")

def delete_video(videos): # method 4
    
    print("--- Which video you want to delete? || Select video number ---")
    list_all_videos(videos)
    video_index = int(input("Enter video index number - "))
    
    option_checker = int(input("Are you sure? Press 1(YES) / Press 0(NO) - "))
    
    # delete a dictionary from the list of dictionary
    
    if 1 <= video_index <= len(videos) and option_checker == 1:
        del videos[video_index-1]
        print(" --- Video deleted successfully ---")
        save_data_helper(videos) ## updates the database
        print(" --- Updated List ---")
        list_all_videos(videos)
    elif 1 <= video_index <= len(videos) and option_checker == 0:
        print(" --- Video is not deleted --- ") 
        
    else:
        print("Invalid index selected")

def main():
    
    videos = load_data() # load database
    
    while True:
        print("\n Welcome to Youtube Manager App || Choose one of the following options")
        print('1. List of favourite videos')
        print('2. Add a video')
        print('3. Update a video detail')
        print('4. Delete a youtube video')
        print('5. Exit the program')
        choice = int(input("Enter your choice (press any from 1 to 5) : "))
        print("*" * 50)
        
        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4: 
                delete_video(videos)
            case 5:
                print("Thank you!")
                break
            case _:
                print("Invalid Choice")
        

if __name__ == "__main__":
    main()