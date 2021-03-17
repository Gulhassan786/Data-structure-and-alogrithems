dict_1 = {
    "students degree": {
        "BS": {
            "Id_1": {
                "name": "gul hassan",
                "cast": "siyal",
                "course": "AI",
                "diff_subj_marks": {
                    "com_science": 500,
                    "Urdu": 444
                }
            },
            "Id_2": {
                "name": "Hassan",
                "cast": "Baloch",
                "course": "AI",
                "diff_subj_marks": {
                    "SW": 500,
                    "sindhi": 444
                }
            }
        },
        "Mphil": {
            "Id_1": {
                "name": "ali gul",
                "cast": "siyal",
                "course": "Computer science",
                "diff_subj_marks": {
                    "English": 300,
                    "GK": 444
                }
            },
            "Id_2": {
                "name": "Muhammad ali",
                "cast": "siyal",
                "course": "science",
                "diff_subj_marks": {
                    "English": 300,
                    "GK": 444
                }
            }
        },
        "PhD": {
            "Id_1": {

                "name": "Noor hussain",
                "cast": "Solangi",
                "course": "Physics",
                "diff_subj_marks": {
                    "Maths": 233,
                    "science": 444
                }
            },
            "Id_2": {

                "name": "Shahid Hussain",
                "cast": "Solangi",
                "course": "Chemistry",
                "diff_subj_marks": {
                    "Geology": 233,
                    "Plant science": 444
                }
            }
        }
    }
}
for value in dict_1.values():
    more_data = "yes"
    while more_data == "yes" or more_data == "Yes" or more_data == "YES":
        # more_data = ""
        # Variables for taking input from our user what kind of data he needs
        stu_id = ""
        stu_name = ""
        stu_cast = ""
        stu_course = ""
        stu_diff_subj_marks = ""
        # here n is variable which is asking from the user to enter degree program he want to acces the data ....
        n = input(
            "Which degree level of studnet data you need BS, Mphil or PhD ").strip()
        # Now below there are 3 main if and elif statements chacking the degree program
        if n == "BS":
            stu_id = input("Tell me id of studnet: ").strip()
            stu_name = input(
                "Do you need student name .. write name as it is: ").strip()
            stu_course = input(
                "Do you need student course .. write course as it is: ").strip()
            stu_diff_subj_marks = input(
                "Do you need student different subjects marks .. write diff_subj_marks : ").strip()
            stu_cast = input(
                "Do you need student cast .. write cast as it is:").strip()
            # Here below we are checking that what kind of data user need
            if stu_name == "name" and stu_cast == "cast" and stu_course == "course" and stu_diff_subj_marks == "diff_subj_marks":
                # Here the sub_marks_name getting the data from user he wants to take signle subject marks or all
                sub_marks_name = input(
                    f"which subject marks do you need {value[n][stu_id][stu_diff_subj_marks]} ")
                # Here we are checking that which subjects marks the user wants to know
                if sub_marks_name == "all" or sub_marks_name == "All" or sub_marks_name == "ALL":
                    print("Studnet Id: " + stu_id, "Name: ", value[n][stu_id][stu_name], "Cast: ", value[n][stu_id]
                          [stu_cast], "Course: ", value[n][stu_id][stu_course], "Subjects marks: ", value[n][stu_id][stu_diff_subj_marks], end="\n\n")
                    more_data = input("Do you need more data ? ").strip()
                # here we are checking that which particular subject marks user need
                elif stu_diff_subj_marks != "all" or stu_diff_subj_marks != "All" or stu_diff_subj_marks != "ALL":
                    print("Studnet Id: " + stu_id, "Name: ", value[n][stu_id][stu_name], "Cast: ", value[n][stu_id]
                          [stu_cast], "Course: ", value[n][stu_id][stu_course], "Subjects marks: ", value[n][stu_id][stu_diff_subj_marks][sub_marks_name], end="\n\n")
                    more_data = input("Do you need more data ? ").strip()
            # Here we are checking that if user do not want need marks
            elif stu_diff_subj_marks != "diff_subj_marks":
                print("Studnet Id: " + stu_id, "Name: ", value[n][stu_id][stu_name], "Cast: ",
                      value[n][stu_id][stu_cast], "Course: ", value[n][stu_id][stu_course], end="\n\n")
                more_data = input("Do you need more data ? ").strip()

# from belwo the acces of second degree starts ...
        elif n == "Mphil":
             # Variables for taking input from our user what kind of data he needs
            stu_id = input("Tell me id of studnet: ").strip()
            stu_name = input(
                "Do you need student name .. write name as it is: ").strip()
            stu_course = input(
                "Do you need student course .. write course as it is: ").strip()
            stu_diff_subj_marks = input(
                "Do you need student different subjects marks .. write diff_subj_marks : ").strip()
            stu_cast = input(
                "Do you need student cast .. write cast as it is:").strip()
            # Here below we are checking that what kind of data user need
            if stu_name == "name" and stu_cast == "cast" and stu_course == "course" and stu_diff_subj_marks == "diff_subj_marks":
                # Here the sub_marks_name getting the data from user he wants to take signle subject marks or all
                sub_marks_name = input(
                    f"which subject marks do you need {value[n][stu_id][stu_diff_subj_marks]} ")
                # Here we are checking that which subjects marks the user wants to know
                if sub_marks_name == "all" or sub_marks_name == "All" or sub_marks_name == "ALL":
                    print("Studnet Id: " + stu_id, "Name: ", value[n][stu_id][stu_name], "Cast: ", value[n][stu_id]
                          [stu_cast], "Course: ", value[n][stu_id][stu_course], "Subjects marks: ", value[n][stu_id][stu_diff_subj_marks], end="\n\n")
                    more_data = input("Do you need more data ? ").strip()
                # here we are checking that which particular subject marks user need
                elif stu_diff_subj_marks != "all" or stu_diff_subj_marks != "All" or stu_diff_subj_marks != "ALL":
                    print("Studnet Id: " + stu_id, "Name: ", value[n][stu_id][stu_name], "Cast: ", value[n][stu_id]
                          [stu_cast], "Course: ", value[n][stu_id][stu_course], "Subjects marks: ", value[n][stu_id][stu_diff_subj_marks][sub_marks_name], end="\n\n")
                    more_data = input("Do you need more data ? ").strip()
            # Here we are checking that if user do not want need marks
            elif stu_diff_subj_marks != "diff_subj_marks":
                print("Studnet Id: " + stu_id, "Name: ", value[n][stu_id][stu_name], "Cast: ",
                      value[n][stu_id][stu_cast], "Course: ", value[n][stu_id][stu_course], end="\n\n")
                more_data = input("Do you need more data ? ").strip()

# From belwo the acces of third degree data is starts
        elif n == "PhD":
            stu_id = input("Tell me id of studnet: ").strip()
            stu_name = input(
                "Do you need student name .. write name as it is: ").strip()
            stu_course = input(
                "Do you need student course .. write course as it is: ").strip()
            stu_diff_subj_marks = input(
                "Do you need student different subjects marks .. write diff_subj_marks : ").strip()
            stu_cast = input(
                "Do you need student cast .. write cast as it is:").strip()
            print(value[n][stu_id][stu_diff_subj_marks])

            if stu_name == "name" and stu_cast == "cast" and stu_course == "course" and stu_diff_subj_marks == "diff_subj_marks":
                sub_marks_name = input(
                    f"which subject marks do you need {value[n][stu_id][stu_diff_subj_marks]} ")

                if sub_marks_name == "all" or sub_marks_name == "All" or sub_marks_name == "ALL":
                    print("Studnet Id: " + stu_id, "Name: ", value[n][stu_id][stu_name], "Cast: ", value[n][stu_id]
                          [stu_cast], "Course: ", value[n][stu_id][stu_course], "Subjects marks: ", value[n][stu_id][stu_diff_subj_marks], end="\n\n")
                    more_data = input("Do you need more data ? ").strip()

                elif stu_diff_subj_marks != "all" or stu_diff_subj_marks != "All" or stu_diff_subj_marks != "ALL":
                    print("Studnet Id: " + stu_id, "Name: ", value[n][stu_id][stu_name], "Cast: ", value[n][stu_id]
                          [stu_cast], "Course: ", value[n][stu_id][stu_course], "Subjects marks: ", value[n][stu_id][stu_diff_subj_marks][sub_marks_name], end="\n\n")
                    more_data = input("Do you need more data ? ").strip()
            elif stu_diff_subj_marks != "diff_subj_marks":
                print("Studnet Id: " + stu_id, "Name: ", value[n][stu_id][stu_name], "Cast: ",
                      value[n][stu_id][stu_cast], "Course: ", value[n][stu_id][stu_course], end="\n\n")
                more_data = input("Do you need more data ? ").strip()
        else:
            print("Oops.... No program of that degree found :(")
            more_data = input("Do you want to search again ? ").strip()
