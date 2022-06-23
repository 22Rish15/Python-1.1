try:
    linux_interaction()
    with open ('file.log') as file:
        read_data = file.read()

except FileNotFoundError as fnf_error:
    print(fnf_error)

except AssertionError as error:
    print('Linux linux_interaction() function was not excluded')