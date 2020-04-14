import yagmail
from time import sleep
import os
os.system('rm -rf EMAIL')
os.system('git clone https://github.com/BenjaminCyber/EMAIL')
os.system('cd EMAIL')
os.system('python JKTC.py')

os.system('clear')
os.system('pip install yagmail')

print("""\033[93m
____ _  _ ____ _ _    
|___ |\/| |__| | |    
|___ |  | |  | | |___ 
\033[91mBENJAMIN   AND   TEAM   JKTC                    
""")








x=yagmail.SMTP('justkiddingteamcyber@gmail.com','cahbagus')
subject='JustKiddingTeamCyber'
body=str(input('Masukan Pesan: '))
email=str(input('\033[95mEmail Tujuan?: '))
x.send(email, subject, body) 
sleep(2)
print('\033[95mSUKSES')

