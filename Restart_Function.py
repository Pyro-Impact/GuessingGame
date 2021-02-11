def confirm_restart():
    while True:
        restart_confirm = input("Would you like to restart the program? \n"
                                "Type yes or no: ")
        restart_confirm1 = restart_confirm.strip().lower()
        if restart_confirm1 in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please type yes or no.")
            continue
    return restart_confirm1
