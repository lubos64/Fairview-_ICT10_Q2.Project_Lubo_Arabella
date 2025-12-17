from pyscript import display, document


def club_info(e):
    select_club = int(document.getElementById("select").value)
    club_advi = {"Communications Arts Club":"Ms. Yannis Fernandez",  
                  "Science Club": "Ms. Jameelyn Maramag",
                  "Math Club": "Mr. Nicole Gabuya",
                  "Social Science Club": "Mr. Roberto Lim",
                  "Marching Band": "Mr. Emilio Alumno",
                  "COCC": "SSgt. Jemima David PA",
                  "Glee Club": "Mr. Denver Martin",
                  "Dance Club": "Mr. Alfred Cases",
                  "Volleyball Varsity": "Mr. Adrian Ruiz",
                  "Basketball Varsity": "Mr. Adrian Ruiz"
                }#Dictionary, Using this to show the advisor of each club
    club_Time = {"Communications Arts Club":"Wednesday 03:00 - 04:00 PM, Friday 03:00 - 04:00 PM", 
                  "Science Club": "Tuesday  03:00 - 04:00 PM",
                  "Math Club": "Monday 02:30- 03:00 PM",
                  "Social Science Club": "Tuesday 03:00 - 4:00 PM",
                  "Marching Band": "Tuesday and Wednesday 03:00-4:30 PM",
                  "COCC": "Wednesday 02:30 -04:30 PM",
                  "Glee Club": "Monday 03:00- 05:00 PM",
                  "Dance Club": "Tuesday 03:00 - 05:00 PM",
                  "Volleyball Varsity": "Wednesday 03:00 - 04:00 PM",
                  "Basketball Varsity": "Monday 03:00 - 04:00 PM"
                }#to show the what time does the club starts

    club_Location = {"Communications Arts Club":"Room 406", #to show where
                  "Science Club": "Room 404",
                  "Math Club": "Room 404",
                  "Social Science Club": "Room 409",
                  "Marching Band": "Band Room",
                  "COCC": "Quadrangle/ Teatro Preciosa ",
                  "Glee Club": "High School Music Room",
                  "Dance Club": "Teatro Preciosa",
                  "Volleyball Varsity": " Quadrangle",
                  "Basketball Varsity": "Quadrangle"
                }

    club_dep = {"Communications Arts Club":"A place to communicate with others and share each other's creative ideas", 
                  "Science Club": "A club for people who wants to explore science more",
                  "Math Club": "A club for Math lovers",
                  "Social Science Club": "A place to discuss your own thoughts to others",
                  "Marching Band": "A club for people who loves to play their intruments",
                  "COCC": "A club for people who wants to keep things in order",
                  "Glee Club": "A place for people who loves to sing",
                  "Dance Club": "A club for people who loves to groove",
                  "Volleyball Varsity": "A place to have fun with others while playing volleyball",
                  "Basketball Varsity": "A place to have fun with others while playing basketball"
                }

    club_members = {"Communications Arts Club":"20",
                  "Science Club": "25",
                  "Math Club": "20",
                  "Social Science Club": "20",
                  "Marching Band": "30",
                  "COCC": "20",
                  "Glee Club": "25",
                  "Dance Club": "25",
                  "Volleyball Varsity": "15",
                  "Basketball Varsity": "15"
                }

        #to show the results on what club you selected
    if select_club == 1:  
        display(f"""Communications Arts Club\n
 
Meeting time: {club_Time["Communications Arts Club"]}\n
Location: {club_Location["Communications Arts Club"]}\n
Number of members:{club_members["Communications Arts Club"]}\n
Advisor: {club_advi["Communications Arts Club"]}\n
Category: Academic\n
Description: {club_dep["Communications Arts Club"]}""", target= "info_output", append = False)# showing results on the id = info_output on the index.html


#for some reason it won't work if I use "else if" but I aksed some help from my classmate, so I used "elif" instead
    elif select_club == 2: 
        display(f"""Science Club\n
 
Meeting time: {club_Time["Science Club"]}\n
Location: {club_Location["Science Club"]}\n
Number of members:{club_members["Science Club"]}\n
Advisor: {club_advi["Science Club"]}\n
Category: Academic\n
Description: {club_dep["Science Club"]}""", target= "info_output", append = False)

    elif select_club == 3:
        display(f"""Math Club\n
 
Meeting time: {club_Time["Math Club"]}\n
Location: {club_Location["Math Club"]}\n
Number of members:{club_members["Math Club"]}\n
Advisor: {club_advi["Math Club"]}\n
Category: Academic\n
Description: {club_dep["Math Club"]}""", target= "info_output", append = False)

    elif select_club == 4:
        display(f"""Social Science Club\n
 
Meeting time: {club_Time["Social Science Club"]}\n
Location: {club_Location["Social Science Club"]}\n
Number of members:{club_members["Social Science Club"]}\n
Advisor: {club_advi["Social Science Club"]}\n
Category: Academic\n
Description: {club_dep["Social Science Club"]}""", target= "info_output", append = False)

    elif select_club == 5:
        display(f"""Marching Band\n
 
Meeting time: {club_Time["Marching Band"]}\n
Location: {club_Location["Marching Band"]}\n
Number of members:{club_members["Marching Band"]}\n
Advisor: {club_advi["Marching Band"]}\n
Category: Non Academic\n
Description: {club_dep["Marching Band"]}""", target= "info_output", append = False)

    elif select_club == 6:
        display(f"""COCC\n
 
Meeting time: {club_Time["COCC"]}\n
Location: {club_Location["COCC"]}\n
Number of members:{club_members["COCC"]}\n
Advisor: {club_advi["COCC"]}\n
Category: Non Academic\n
Description: {club_dep["COCC"]}""", target= "info_output", append = False)

    elif select_club == 7:
        display(f"""Glee Club\n
 
Meeting time: {club_Time["Glee Club"]}\n
Location: {club_Location["Glee Club"]}\n
Number of members:{club_members["Glee Club"]}\n
Advisor: {club_advi["Glee Club"]}\n
Category: Non Academic\n
Description: {club_dep["Glee Club"]}""", target= "info_output", append = False)


    elif select_club == 8:
        display(f"""Dance Club\n
 
Meeting time: {club_Time["Dance Club"]}\n
Location: {club_Location["Dance Club"]}\n
Number of members:{club_members["Dance Club"]}\n
Advisor: {club_advi["Dance Club"]}\n
Category: Non Academic\n
Description: {club_dep["Dance Club"]}""", target= "info_output", append = False)


    elif select_club == 9:
        display(f"""Volleyball Varsity\n
 
Meeting time: {club_Time["Volleyball Varsity"]}\n
Location: {club_Location["Volleyball Varsity"]}\n
Number of members:{club_members["Volleyball Varsity"]}\n
Advisor: {club_advi["Volleyball Varsity"]}\n
Category: Non Academic\n
Description: {club_dep["Volleyball Varsity"]}""", target= "info_output", append = False)

    elif select_club == 10:
        display(f"""Basketball Varsity\n

Meeting time: {club_Time["Basketball Varsity"]}\n
Location: {club_Location["Basketball Varsity"]}\n
Number of members:{club_members["Basketball Varsity"]}\n
Advisor: {club_advi["Basketball Varsity"]}\n
Category: Non Academic\n
Description: {club_dep["Basketball Varsity"]}""", target= "info_output", append = False)

    




