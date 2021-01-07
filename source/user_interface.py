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

def get_output_file() :
    output_file = input("  Enter the path to the output file : ")
    print("")

    return output_file

def choose_option(choose_name, options_list) :
    print("  " + choose_name + " :")
    for i in range(len(options_list)) :
        print("  \t" + str(i + 1) + ". " + options_list[i])

    print("")

    while True :
        answer = int(input("  Enter your answer : "))

        if answer <= 0 or answer > len(options_list) :
            print("  [ERROR] Incorrect number. Try again")
            print("")
        else :
            return answer