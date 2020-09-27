import random
import sqlite3


class Password:
    ''' Create a class for Password passing the account name for it '''

    alpha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k',
             'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'y', 'x', 'z')

    alpha_upper = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
                   'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'Y', 'X', 'Z')

    numerical = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    symbols = ('?', '!', ',', '.', '/', '(', ')', '*', '<', '>')

    def __init__(self, account):
        self.account = account

    @staticmethod
    def alphabetical(length):
        ''' Only letters both capital and lower case '''
        out = False
        alphabet = Password.alpha + Password.alpha_upper
        while not out:
            # print('inside 1st loop')
            count = 0
            password = ''
            for i in range(length):
                ran_items = random.sample(alphabet, 1)
                if len(password) >= 1:
                    if ran_items != password[count]:
                        password += ran_items[0]
                    else:
                        continue
                else:
                    password = ran_items[0]
            if any(letter in alphabet for letter in password):
                out = True
                # print('out of 1st loop')
            else:
                continue
        return password

    @staticmethod
    def alphanumerical(length):
        ''' Combination of letters and numbers '''
        out = False
        alpha_numerical = Password.alpha + Password.alpha_upper + Password.numerical
        while not out:
            # print('inside 1st loop')
            count = 0
            password = ''
            for i in range(length):
                ran_items = random.sample(alpha_numerical, 1)
                if len(password) >= 1:
                    if ran_items != password[count]:
                        password += ran_items[0]
                    else:
                        continue
                else:
                    password = ran_items[0]
            if any(letter in Password.numerical for letter in password):
                out = True
                # print('out of 1st loop')
            else:
                continue
        return password

    @staticmethod
    def highsecurity(length):
        ''' Combination of letter, numbers and symbols '''
        out = False
        high_security = Password.alpha + Password.alpha_upper + Password.numerical + Password.symbols
        while not out:
            # print('inside 1st loop')
            count = 0
            password = ''
            for i in range(length):
                ran_items = random.sample(high_security, 1)
                if len(password) >= 1:
                    if ran_items != password[count]:
                        password += ran_items[0]
                    else:
                        continue
                else:
                    password = ran_items[0]
            if any(letter in Password.symbols for letter in password):
                out = True
                # print('out of 1st loop')
            else:
                continue
        return password


conn = sqlite3.connect('keychain.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Keychain (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    account_name, 
                                    password) ''')

acc_input = input('Enter the account: ')
acc1 = Password(acc_input)
keyword = acc1.highsecurity(12)

if len(acc_input) == 0:
    print('No input')
    quit()
else:
    try:
        cur.execute('SELECT * FROM Keychain WHERE account_name=?', (acc_input,))
        cur.execute('UPDATE Keychain SET password=(?) WHERE account_name=(?)', (keyword, acc_input))
    except:
        cur.execute('INSERT INTO Keychain (account_name, password) VALUES (?, ?)', (acc_input, keyword))

    conn.commit()

cur.close()

print(acc1.account)
print(keyword)
