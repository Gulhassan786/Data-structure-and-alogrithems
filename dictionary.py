dict_1 = {
    "students": {
        "Id_1": {
            "name": "gul hassan",
            "cast": "siyal",
            "course": "AI",
        },
        "Id_2": {
            "name": "ali gul",
            "cast": "siyal",
            "course": "Nothing"
        },
        "Id_3": {
            "name": "Noor hussain",
            "cast": "Solangi",
            "course": "Physics"
        }
    }
}
for keys, value in dict_1.items():

    for i in range(len(value)):
        more_data = ""
        n = input("Tell me id of the student: ").strip()
        print("Name: " + value[n]["name"],
              "Course: " + value[n]["course"], end="\n\n")
        more_data = input("do you need more data ?")
        if more_data == "no" or more_data == "No" or more_data == "NO":
            print("Ok.. process is completed :)")
            break
        elif more_data == "yes" or more_data == "Yes" or more_data == "YES":
            n = input("Tell me id of the student: ").strip()
            print("Name: " + value[n]["name"],
                  "Course: " + value[n]["course"], end="\n\n")


#dic = {key : value}
