#login for users 
#pip install pystyle
from pystyle import *





print(Box.Lines("[+] my first project using python  [+]"))
Write.Print("[+]welcome to my first program \n" , Colors.purple_to_red,interval=0.1)
Write.Print("[+]Write user name and password \n \n " , Colors.purple_to_red,interval=0.1)
print(Box.DoubleCube("Example [1]"))

while True:
    username = Write.Input('write username : ', Colors.blue_to_green , interval=0.1)
    passward = Write.Input('write password : ', Colors.blue_to_green , interval=0.1)

    if username == 'Gehad' and passward == '123456789':
        Write.Print('[+] welcome Admin \n ', Colors.green , interval=0.1)
        input('\n press any key to exit....')
    else:
        Write.Print(" [-] Error Try again \n\n ", Colors.red , interval=0.1)    




