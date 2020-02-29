def is_username_valid(username):
    int_1 = int(username[0])
    int_2 = int(username[-1])
    if (username.islower()) & (type(int_1) == int) & (type(int_2) == int) & (len(username) > 5) & (len(username) < 8) & (username[0] == username[-1]):
        return True
    else:
        return False
    
def is_password_valid(username):
    username_list = []
    str_list = []
    int_list = []
    for i in username:
        username_list.append(i)
        try: 
            int(i)
            int_list.append(int(i))
        except ValueError:
            str_list.append(i)
            
    del str_list[str_list.index('-')]
    print(str_list)

    if (username.islower()) & (len(str_list) == len(int_list)) & (len(username) > 7) & (len(username) < 11) & ('-' in username):
        return True
    else:
        return False
        