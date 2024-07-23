# assigning date format
from datetime import datetime
date_format = "%d-%m-%Y"

# main menu variables
choice = 0

# new project variables
project = []
name = []
start_date_input = []
end_date_input = []
available = 1000  # assigning available workers as 1000
workers = 0
status = []
save = 0

# remove project variables
remove = 0
actual_date = 0

# add workers variables
workers_add = 0
add = 0

# update details variables
n_name = 0
n_start_date = 0
n_end_date = 0
n_workers = 0
n_status = 0

# main lists
ongoing_projects = []
completed = []
hold = []


# Main Menu UI
def main_menu():
    global choice
    print("                                                                  XYZ Company")
    print("                                                                    Main Menu")
    print()
    print("1. Add a new project to existing projects.")
    print("2. Remove a completed project from existing projects.")
    print("3. Add new workers to available workers group.")
    print("4. Update details on ongoing projects.")
    print("5. Project Statistics")
    print("6. Exit")
    print()

    while True:  # for an invalid choice, prompt for a new selection
        try:
            choice = int(input(
                "                                                                                                    Your Choice:"))
            if choice not in range(1, 7) or choice == 0:  # checks for the choice in the range between 1 and 6
                print("Integer inputs between 1 to 6 are accepted.")
            else:
                break
        except ValueError:  # checks if the user gives a string input
            if isinstance(choice, int):
                print("String inputs are not accepted.")
            else:
                break


# New project UI
def new_project():
    global ongoing_projects
    global available

    print("                                                                  XYZ Company")
    print("                                                               Add a new project")
    print()
    print("                                                       **Enter'0' to Project code to exit.")

    while True:  # for an invalid project code, prompt for a new code
        try:
            project = int(input("Project Code-"))
            if isinstance(project, int):  # verifies the input for the project code as an integer
                break
        except:
            print("Project code should be an integer input")
    if project == 0:
        return main_menu()
    name = str(input("Clients Name-"))

    while True:  # for an invalid date, prompt for a new date
        try:
            start_date_input = str(input("Start date-"))
            start_date = datetime.strptime(start_date_input, date_format).date()  # converts string input to date format
            end_date_input = str(input("Expected end date-"))
            end_date = datetime.strptime(end_date_input, date_format).date()
            if start_date == end_date:  # if start date and expected end date entered same date
                print("Starting date and Expected end date are same.")
            elif start_date < end_date:  # if expected end date entered a date before start date
                break
            else:
                print("Expected End date should be a date after Start date")
        except ValueError:
            print(
                "Invalid Date format;only %d-%m-%Y datetime format is accepted.")

    while True:  # for an invalid input for workers, prompt for a valid input
        try:
            workers = int(input("Number of workers-"))
            if workers < 0:  # verifying for negative input for workers
                print("Workers cannot be a negative number;positive integer input expected.")
            else:
                break
        except ValueError:  # string input for workers
            print("Number of workers should be an integer input; string inputs are not accepted")

    if available < workers:  # validates worker availability
        print("Workers available for a new project are less than the required number;Project cannot be taken.")
        return main_menu()
    else:
        print("Required number of workers are available.")
        available = available - workers  # updating the available number of workers

    while True:
        status = str(input("Project Status (ongoing, on hold or completed)-"))
        if status.lower() == "ongoing":
            break
        elif status.lower() == "on hold":  # when taking new project, status cannot be on hold
            print("Status of a new project cannot be 'on hold'.")
        elif status.lower() == "completed":  # new project cannot be completed
            print("Status of a new project cannot be 'completed'.")
        else:  # validate inputs for status (string or integer)
            print("Invalid response; choose a valid string response (ongoing, on hold or completed)-")
    print()
    print()

    while True:
        save = str(input("Do you want to save the project(Yes/No)?")).lower()
        if save == "yes":
            ongoing_projects.append(project)  # appending to ongoing projects list
            ongoing_projects.append(name)
            ongoing_projects.append(start_date_input)
            ongoing_projects.append(end_date_input)
            ongoing_projects.append(workers)
            ongoing_projects.append(status)
            print("Project", project, "saved Successfully.")  # notifying user
            return new_project()
        elif save == "no":
            print("Adding a new project cancelled successfully.")
            main_menu()
        else:  # validate inputs for save (integer or string)
            print("Only string inputs are accepted;choose from (Yes/No) options.")


# remove project interface
def remove_project():
    global available
    print("                                                                 XYZ Company")
    print("                                                           Remove Completed Project")
    # checking if the list is empty
    if len(ongoing_projects) != 0:  # checking whether there are any projects saved in ongoing projects
        while True:
            try:
                project = int(input("Project Code-"))
                if isinstance(project, int):  # verifies integer input for project code
                    if project in ongoing_projects:  # project code in the ongoing projects list
                        break
                    else:
                        print("Project code:", project, "not found in the ongoing projects list.")
                else:
                    print("Project code should be an integer input")
            except:
                print("Project code should be an integer input")
        while True:
            remove = str(input("Do you want to remove the project(Yes/No)?")).lower()
            if remove == "yes":
                project_index = ongoing_projects.index(project)  # finding the index of the entered project code

                name = ongoing_projects[project_index + 1]
                start_date_input = ongoing_projects[project_index + 2]
                end_date_input = ongoing_projects[project_index + 3]
                start_date = datetime.strptime(start_date_input, date_format).date()
                end_date = datetime.strptime(end_date_input, date_format).date()
                while True:
                    try:
                        actual_date_input = str(input("Enter the actual end date-"))  # taking the actual end date
                        actual_date = datetime.strptime(actual_date_input, date_format).date()

                        if actual_date > end_date:
                            print("Project", project, "completed after the expected end date.")
                            break
                        elif actual_date == end_date:
                            print("Project", project, "completed on the expected end date.")
                            break
                        else:
                            print("Project", project, "completed before the expected end date.")
                            break
                    except ValueError:
                        print("Invalid Date format;only %d-%m-%Y datetime format is accepted.")

                workers = ongoing_projects[project_index + 4]
                status = ongoing_projects[project_index + 5]
                status = "completed"  # changing status to completed when moving to completed projects

                # assigning project details to completed projects
                completed.extend([project, name, start_date_input, end_date_input, workers, status, actual_date_input])
                del ongoing_projects[project_index:project_index + 6]  # removing from ongoing projects
                available = available + workers  # releasing the workers in that project
                print("Project", project, "removed from ongoing projects and added to completed projects")
                return main_menu()
            elif remove == "no":
                print("Removing project", project, "cancelled successfully.")
                return main_menu()
            else:
                print("Only string inputs are accepted;choose from (Yes/No) options.")
    else:
        print("No saved projects;empty list")
        main_menu()


# new workers interface
def new_workers():
    global available
    print("                                                                   XYZ Company")
    print("                                                                 Add New Workers")
    while True:
        try:  # checks for a string input for workers
            workers_add = int(input("Number of workers to add-"))  # taking number of workers to add
            if workers_add < 0:  # checks for a negative integer input
                print("Positive Integer inputs are expected.")
            else:
                break
        except ValueError:
            print("Integer inputs are accepted;Check your input data type")
    print()
    print()
    while True:
        add = str(input("Do you want to add(Yes/No)?")).lower()
        if add == "yes":
            available += workers_add  # adding new workers to available workforce
            print("New", workers_add, "workers added to available workers Successfully.")
            print("New number of available workers are:", available)
            return main_menu()
        elif add == "no":
            print("Adding new workers cancelled successfully.")
            return main_menu()
        else:  # check for integer or other string inputs for the add
            print("Only string inputs are accepted;choose from (Yes/No) options.")


# update details interface
def update_details():
    global available
    print("                                                                 XYZ Company")
    print("                                                           Update Project Details")
    print("                                                     **Enter '0' to Project Code to exit")

    if len(ongoing_projects) != 0:  # checking whether there are projects in the ongoing projects to update
        while True:
            try:
                project = int(input("Project Code-"))
                if isinstance(project, int):  # verifies integer input for project code
                    if project in ongoing_projects:  # check the project code in the ongoing projects list
                        print("Details found under the project", project)
                        break
                    elif project == 0:
                        return main_menu()
                    else:
                        print("No details found under the project", project)
                else:
                    print("Project code should be an integer input")
            except:
                print("Project code should be an integer input")

        n_name = str(input("Clients Name-"))
        while True:
            date_format = "%d-%m-%Y"
            try:
                n_start_date = str(input("Start date-"))
                start_date = datetime.strptime(n_start_date, date_format).date()  # converts string input to date format
                n_end_date = str(input("Expected end date-"))
                end_date = datetime.strptime(n_end_date, date_format).date()
                if start_date == end_date:
                    print("Starting date and Expected end date are same.")
                elif start_date < end_date:
                    break
                else:
                    print("Expected End date should be a date after Start date")
            except ValueError:
                print(
                    "Invalid Datetime format;%d-%m-%Y datetime format is accepted.")

        while True:
            try:
                n_workers = int(input("Number of workers-"))
                if n_workers < 0:  # verifying for negative input for workers
                    print("Workers cannot be a negative number;positive integer input expected.")
                elif available < n_workers:
                    print("available number of workers are:", available)
                    print("Enter  less than available number of workers.")
                elif available > n_workers:
                    print("Required number of workers are available.")
                    break
                else:
                    break
            except ValueError:
                print("Number of workers should be an integer input; string inputs are not accepted")
        n_status = str(input("Project Status (ongoing/on hold/completed)-"))
        while True:
            if n_status.lower() in ["ongoing", "on hold", "completed"]:
                if n_status == "completed":  # navigate user to remove completed project
                    print("The project", project, "should move to completed projects list.")
                    return remove_project()
                break
            else:
                n_status = str(input("Invalid response; choose a valid string input (ongoing, on hold or completed)- "))
        print()
        print()
        save = str(input("Do you want to save the project(Yes/No)_?")).lower()
        if save == "yes":
            update_index = ongoing_projects.index(project)
            if n_status == "ongoing":
                ongoing_projects[update_index + 1] = n_name
                ongoing_projects[update_index + 2] = n_start_date
                ongoing_projects[update_index + 3] = n_end_date
                available += ongoing_projects[update_index + 4]  # re-assigning saved workers to available workers
                ongoing_projects[update_index + 4] = n_workers
                available = abs(available - n_workers)  # subtracting the new amount from the available workers
                ongoing_projects[update_index + 5] = n_status
                print("Details of project", project, "updated Successfully.")

            elif n_status == "on hold":
                ongoing_projects[update_index + 1] = n_name
                ongoing_projects[update_index + 2] = n_start_date
                ongoing_projects[update_index + 3] = n_end_date
                available += ongoing_projects[update_index + 4]
                ongoing_projects[update_index + 4] = n_workers
                available = abs(available - n_workers)
                ongoing_projects[update_index + 5] = n_status

                # moving to on-hold project
                hold.extend([project, n_name, n_start_date, n_end_date, n_workers, n_status, ])

                # removing from ongoing projects
                del ongoing_projects[update_index:update_index + 6]
                print("Details of Project", project, "updated and added to the on hold projects list successfully.")
            else:
                print()
        elif save == "no":
            print("Updating details of project", project, "cancelled successfully. ")
            return main_menu()
        else:
            print("Only string inputs are accepted;choose from (Yes/No) options.")
    else:
        print("No project details found;No saved projects.")
        return main_menu()


# statistics interface
def statistics():
    print("                                                                         XYZ Company")
    print("                                                                     Project Statistics")
    print("Number of ongoing projects-", int(len(ongoing_projects) / 6))
    print("Number of completed projects-", int(len(completed) / 6))
    print("Number of on hold projects-", int(len(hold) / 6))
    print("Number of available workers to assign-", available)
    while True:
        add_project = str(input("Do you want to add the project(Yes/No)?_")).lower()
        if add_project == "yes":
            return new_project()
        elif add_project == "no":
            break
        else:
            print("Only string inputs are accepted;choose from (Yes/No) options.")
    main_menu()


# program end
def program_end():
    exit()


main_menu()
while True:
    if choice == 1:
        new_project()
    if choice == 2:
        remove_project()
    if choice == 3:
        new_workers()
    if choice == 4:
        update_details()
    if choice == 5:
        statistics()
    if choice == 6:
        program_end()
