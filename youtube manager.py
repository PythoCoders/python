videos = []


def Add_a_video():
    name = input("Enter the name of video:")
    time = input("Enter the length of video(Duration):")
    # with open('YOUTUBE.txt','w') as file:
    #     file.write(f"{name} : {time}")
    videos.append(f"{name},Duration: {time}")
    print()
    print("Your video is successfully added!!!")
    print()
    return main()
        
def Rename_video():
    pass

def Delete_video():
    get_option = int(input("Enter the index of video that you want to delete:"))
    pov = len(videos)-get_option
    if get_option == len(videos)-pov:
        videos.remove(videos[get_option - 1])
    else:
        print("Invalid index")
    print()
    print("Your video has deleted successfully!!!")
    return main()

def List():
    print("## Here is the list of all your videos-->")
    print()
    for index,vis in enumerate(videos,start = 1):
       print(f"{index}.{vis}")
    return main()

def main():
    print("*"*100)
    print()
    x = "WELCOME TO THE YOUTUBE MANAGER"
    print(x.center(95))
    print("*"*100)
    print()
    print("""DESCRIPTION: In this tool we have given few services to enhance and improve your youtube journey.
             To choose any function just enter the no alongside each option""")
    print()
    while True:
        print("1. Add a video")
        print("2. Rename a video")
        print("3. Delete a video")
        print("4. List all videos")
        print("5. Exit")
        print()
        choice = input("Enter what you want to do: ")
        print()

        match choice:
            case "1":
               return Add_a_video()
            case "2":
               return Rename_video()
            case "3":
               return Delete_video()
            case "4":
               return List()
            case "5":
                break
               
            case _:
               print("Invalid choice")



if __name__ == "__main__":
    main()