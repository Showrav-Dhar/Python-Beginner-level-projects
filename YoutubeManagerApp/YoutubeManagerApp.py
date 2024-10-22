import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except:
        pass


def list_all_videos(videos):
    pass


def add_video(videos):
    pass


def update_video(videos):
    pass


def delete_video(videos):
    pass


def main():  # program starts from here
    videos = load_data()
    while True:
        print("\nYoutube Manager || Choose an option")
        print("1. List all favourite videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("4. Exit the app")

        choice = input("Enter Your Option")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice, Press something from (1-5)")


if __name__ == '__main__':
    main()
