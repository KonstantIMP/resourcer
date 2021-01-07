import resourcer_defines

import os.path

def print_hello() :
    print("    _  _      \t")
    print("   | || | _   \t RESOURCER\tVersion : " + resourcer_defines.version_str)
    print("  -| || || |  \t")
    print("   | || || |- \t A simple program for creating arrays")
    print("    \\_  || |  \t \t\tof data from file resources")
    print("      |  _/   \t")
    print("     -| | \\   \t Feedback email : mihedovkos@gmail.com")
    print("      |_|-    \t Powered by KonstantIMP")
    print("")

def get_input_file() :
    input_path = input("  Enter the path to the input file : ")

    while True :
        if os.path.exists(input_path) == True :
            if os.path.isfile(input_path) == True :
                print("")
                return input_path
            else :
                print("")
                print("  [ERROR] File \'" + input_path + "\' exists, but it is a FOLDER")
                input_path = input("  Enter the path to the input file : ")
        else :
            print("")
            print("  [ERROR] File \'" + input_path + "\' doesn`t exist")
            input_path = input("  Enter the path to the input file : ")