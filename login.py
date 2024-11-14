import pickle
import os 
users = []
passwords = []
def sign_in():
    user = input('enter your username: ')
    if user in users:
        user_index = users.index(user)
        # user_index = filter(x for x in users if x == 'user')
        password = input('enter the password: ')
        if password == passwords[user_index]:
            global a
            a = 0
            print('Login Success')
        else:
            print('Incorrect Password')
            sign_in()
    else:
        print('User does not exists')
        print('redirecting to sign up')
        sign_up()

def sign_up():
    new_user = input('enter username: ')
    users.append(new_user)
    new_pass = input('enter the password: ')
    passwords.append(new_pass)

def acc_del():
    del_user = input('enter username to delete: ')
    del_pass = input('enter the password to delete: ')
    del_user_index = users.index(del_user)
    if del_pass == passwords[del_user_index]:
        users.remove(del_user)
        passwords.remove(del_pass)
        print('user deleted successfully...')
    else:
        print('Incorrect Password')
        print('User deletion failed...')

def ask():
    ask = int(input(
            '''1. Sign in    
               2. Sign up
               3. Delete an account
            '''))
    if ask == 1:
        sign_in()
    elif ask == 2:    
        sign_up()

        ask()
    elif ask == 3:
        acc_del()

        ask()
    else:
        print("ERROR")
        print('invalid option selected...')

if __name__ == "__main__":
    ask()

#need some improvements