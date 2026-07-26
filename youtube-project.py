videos = []

print("/"*75)
print()
welcome = "Youtube Manager"
print(welcome.center(80))
print()
print("/"*75)
print("This tool hepls you to organize your youtube videos!! Let's get started!!")
print("/"*75)
print()

def add_video():
    name = input("Enter your video name : ")
    time = input("Enter video time : ")
    videos.append(f"{name}, Duration : {time}")
    print("Your video has been added to list!")
    print()
    return main()
    

def veiw_list():
    print("Here is your up-to-date list :-")
    for index,video in enumerate(videos, start=1):
       print(index, video)
       print()
    return main()
        

def rename_video():
    choice = int(input("Enter the index of the video to be renamed : "))
    new_name = input("Enter new name : ")
    new_time = input("Enter new duration : ")
    videos.remove(videos[choice-1])
    videos.insert(choice-1, f"{new_name}, Duration : {new_time}")
    print("Your video has been renamed!")
    print()
    return main()

def delete_video():
    choice = int(input("Enter the index of the video to be deleted : "))
    videos.remove(videos[choice-1])
    print("Your video has been deleted successfully!!")
    print()
    return main()


        
        

def main():
    while True:
        print("MAIN MENU")
        print("1. Add a youtube video")
        print("2. Veiw your list")
        print("3. Rename a video in your list")
        print("4. Delete a video")
        print("5. Exit the tool")
       
        print()
        choice = input("Enter the index to use a function : ")
        print()

        match choice:
            case "1":
                return add_video()
            case "2":
                return veiw_list()
            case "3" :
                return rename_video()
            case "4":
                return delete_video()
            case "5":
                break
           



if __name__ == "__main__":
    main()



        




