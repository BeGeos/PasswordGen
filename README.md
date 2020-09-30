Password-Generator
Password class and methods to create random passwords either alphabetical, alphanumerical or with numbers, letters and symbols (high security). The class is initialised via the account name, so that the password can be linked to an account, and the methods have as atrribute the length of the password.

As a common problem, more websites mean more passwords in use to sign up to. Using the same password can be dangerous, as it could be exploited. Come up with new passwords, always different from the previous ones as well as respecting certain parameters set by the website, length constrains, use of numbers, capitals etc, can really be stressful and time consuming.

A good solution for a basic programmer is to come up with your own password generator. As a metter of fact, it could be use in conjunction with a database where, making use of the class argument account, data can be stored progressively for each account and password, or in a python dictionary as key, value pairs (account:password). In this case, I provided an sqlite file which is the default database of the script, purposely named keychain. 
