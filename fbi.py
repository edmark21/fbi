###################################################################
#                        Import Module
import json , sys , hashlib , os , time , marshal, getpass
import sys,time,os
import mechanize
import cookielib
import random
###################################################################
'''
     Facebook Information 
'''
###################################################################
#                             COLOR

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



if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
        G = '\033[32;1m'
        R = '\033[31;1m'
else:
	W = ''
	G = ''
	R = ''
###################################################################
#                      Exception
try:
	import requests
except ImportError:
	print R + '_     _'.center(44)
	print "o' \.=./ `o".center(44)
	print '(o o)'.center(44)
	print 'ooO--(_)--Ooo'.center(44)
	print W + ' '
	print ('F B I').center(44)
	print ' '
	print "[!] Can't import module 'requests'\n"
	sys.exit()
####################################################################
#                    Set Default encoding
reload (sys)
sys . setdefaultencoding ( 'utf8' )
####################################################################
#       	        I don't know
jml = []
jmlgetdata = []
n = []
####################################################################
#                        BANNER











def baliho():
	try:
		token = open('cookie/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		name = a['name']
		n.append(a['name'])

	except (KeyError,IOError):
		
	    print G
	    print ("\t\t++++++++++++++++++++++++++++++++")
	    print ("\t\t\tFacebook Hack Tool")
	    print W
####################################################################
#		    Print In terminal
def show_program():

	print '''
                    %sINFORMATION%s
 ------------------------------------------------------

    Author     Edmark21
    Name       Facebook Hack Tool
    Version    Beta
    Date       10/02/2019 
    Jabber     warmaker35@gmail.com

* if you find any errors or problems , please contact
  author
'''%(G,W)
def info_ga():

	logo = '''


	mailcheck		Check if email exist or not
	generate		 Generate 3 digit for confirmation code
	brute               Bruteforce Facebook password
	get_data           fetching all friends data
	get_info           show information about your friend

	dump_id            fetching all id from friend list
	dump_phone         fetching all phone number from friend list
	dump_mail          fetching all emails from friend list
	dump_<id>_id       fetching all id from your friends
	<spesific>
	ex: dump_username_id


   clear              clear terminal
   help               show help
   about              Show information about this program
   exit               Exit the program
   
   '''
   
	print logo




def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		baliho()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		main()
def id():
	print '[*] login to your facebook account         ';id = raw_input('[?] Username : ');pwd = getpass.getpass('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)
####################################################################
#       	            BOT
	                # Execute #


	

######################################################################################################################
#			    Bot reaction
  			   # Prepairing #

#
###############################################################################

###############################################################################
#                         Dump Data

def dump_id():

	print '[*] Load Access Token'
	try:
		token = open("cookie/token.log",'r').read()
		print '[*] success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all friends id'
	try:

		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_id.txt','w')
		for i in a['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.0001)

		out.close()
		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_id.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] failed to fetch friend id'
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error                 '
		print '[!] Stopped'
		main()

def dump_phone():
	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print "[*] fetching all phone numbers"
	print '[*] start'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_phone.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
			z = json.loads(x.text)

			try:
				out.write(z['mobile_phone'] + '\n')
				print W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['mobile_phone']
			except KeyError:
				pass
		out.close()
		print '[*] done'
		print "[*] all phone numbers successfuly retrieved"
		print '[*] file saved : output/'+n[0].split(' ')[0] + '_phone.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] failed to fetch all phone numbers"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

def dump_mail():
	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
                print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all emails'
	print '[*] start'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
                a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_mails.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
                        z = json.loads(x.text)

			try:
                                out.write(z['email'] + '\n')
			        print W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['email']
			except KeyError:
				pass
		out.close()

                print '[*] done'
                print "[*] all emails successfuly retrieved"
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_mails.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] failed to fetch all emails"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

def dump_id_id():
	global target_id

	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all id from your friend'

	try:
		r = requests.get('https://graph.facebook.com/{id}?fields=friends.limit(5000)&access_token={token}'.format(id=target_id,token=token))
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt','w')

		for i in a['friends']['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.0001)
		out.close()

		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] failed to fetch friend id'
		try:
			os.remove('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt')
		except OSError:
			pass
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error                      '
		print '[!] Stopped'
		
		
		

		
		
#
###############################################################################2

###############################################################################
#                         Main





def redu():
	print "--------------------------"
	ac = raw_input(R+ "Already Login [y/n]:  " + W)
	print "--------------------------"
	if (ac == 'y'):
		baliho()
	elif (ac == "n"):
		id()
	else:
		print "invalid command"
		redu()
		
redu()
  		




def main():

  global target_id
  
 
  		
  

  try:
  	
  	
  

  	if len(jml) == 0:
  		getdata()
  	
  	
  		
	
	
		
	cek = raw_input(R + 'exploit@fb:  ' + W)

	if cek.lower() == 'get_data':
		if len(jml) == 0:
			getdata()
		else:
			print '[*] You have retrieved %s friends data'%(len(jml))
			main()
	elif cek.lower() == 'get_info':
		print '\n'+'[*] Information Gathering [*]'.center(44) + '\n'
		search()
	#elif cek.lower() == 'brute':
		#print "Not finish yet"
		#main()
	elif cek.lower() == "cat_token":
		try:
			o = open('cookie/token.log','r').read()
			print '[*] Your access token !!\n\n' + o + '\n'
			main()
		except IOError:
			print '[!] failed to open cookie/token.log'
			print "[!] type 'token' to generate access token"
			welcome()

	elif cek.lower() == 'clear':
		if sys.platform == 'win32':
			os.system('cls')
			baliho()
			main()
		else:
			os.system('clear')
			baliho()
			main()
			
	elif cek.lower() == ('brute'):
		print "not finish yet"
		main()
		
		
		

	
	elif cek.lower() == 'exit':
		print "[!] Exiting Program"
		sys.exit()
	elif cek.lower() == 'help':
		info_ga()
		main()
	elif cek.lower() == 'dump_id':
		dump_id()
	elif cek.lower() == 'dump_phone':
		dump_phone()
	elif cek.lower() == 'dump_mail':
		dump_mail()

	if 'dump_' in cek.lower() and cek.lower().split('_')[2] == 'id':
		target_id = cek.lower().split('_')[1]
		dump_id_id()
	else:
		if cek == '':
			main()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "help" to show command'
			main()
  except KeyboardInterrupt:
	main()
  except IndexError:
	print '[!] invalid parameter on command : ' + cek
	main()
#
######################################################################################################################

################################################################################
#                          Get Data





def getdata():
	global a , token

	print '[*] Load Access Token'

	try:
		token = open("cookie/token.log","r").read()
		print '[*] Success load access token '
	except IOError:
		print '[!] failed to open cookie/token.log'
		print "[!] type 'token' to generate access token"
		main()

	print '[*] fetching all friends data'

		

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

	except KeyError:
		print '[!] Your access token is expired'
		print "[!] type 'token' to generate access token"
		main()

	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

	for i in a['data']:
		jml.append(i['id'])
		print '\r[*] fetching %s data from friends'%(len(jml)),;sys.stdout.flush();time.sleep(0.0001)

	print '\r[*] '+str(len(jml))+' data of friends successfully retrieved'
	os.system("clear")
	main()

def search():

	if len(jml) == 0:
                print "[!] no friend data in the database"
                print '[!] type "get_data" to collect friends data'
                main()
        else:
                pass

	target = raw_input("[!] Search Name or Id : ")

	if target == '':
		print "[!] name or id can't be empty !!"
		search()
	else:
		info(target)

def info(target):
        global a , token

        print '[*] Searching'
	for i in a['data']:

	  if target in  i['name'] or target in i['id']:

		x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
		y = json.loads(x.text)

		print ' '
		print G + '[-------- INFORMATION --------]'.center(44)
		print W

		try:
			print '\n[*] Id : '+i['id']
		except KeyError:
			pass
		try:
			print '[*] Username : '+y['username']
		except KeyError:
			pass
		try:
			print '[*] Email : '+y['email']
		except KeyError:
			pass
		try:
			print '[*] Mobile Phone : '+y['mobile_phone']
		except KeyError:
			pass
		try:
			print '[*] Name : '+y['name']
		except KeyError:
			pass
		try:
			print '[*] First name : '+y['first_name']
		except KeyError:
			pass
		try:
			print '[*] Midle name : '+y['middle_name']
		except KeyError:
			pass
		try:
			print '[*] Last name : '+y['last_name']
		except KeyError:
			pass
		try:
			print '[*] Locale : '+y['locale'].split('_')[0]
		except KeyError:
			pass
		try:
			print '[*] location : '+y['location']['name']
		except KeyError:
			pass
		try:
			print '[*] hometown : '+y['hometown']['name']
		except KeyError:
			pass
		try:
			print '[*] gender : '+y['gender']
		except KeyError:
			pass
		try:
			print '[*] religion : '+y['religion']
		except KeyError:
			pass
		try:
			print '[*] relationship status : '+y['relationship_status']
		except KeyError:
			pass
		try:
			print '[*] political : '+y['political']
		except KeyError:
			pass
		try:
			print '[*] Work :'

			for i in y['work']:
				try:
					print '   [-] position : '+i['position']['name']
				except KeyError:
					pass
				try:
					print '   [-] employer : '+i['employer']['name']
				except KeyError:
					pass
				try:
					if i['start_date'] == "0000-00":
						print '   [-] start date : ---'
					else:
						print '   [-] start date : '+i['start_date']
				except KeyError:
					pass
				try:
					if i['end_date'] == "0000-00":
						print '   [-] end date : ---'
					else:
						print '   [-] end date : '+i['end_date']
				except KeyError:
					pass
				try:
					print '   [-] location : '+i['location']['name']
				except KeyError:
					pass
				print ' '
		except KeyError:
			pass
		try:
			print '[*] Updated time : '+y['updated_time'][:10]+' '+y['updated_time'][11:19]
		except KeyError:
			pass
		try:
			print '[*] Languages : '
			for i in y['languages']:
				try:
					print ' ~  '+i['name']
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] Bio : '+y['bio']
		except KeyError:
			pass
		try:
			print '[*] quotes : '+y['quotes']
		except KeyError:
			pass
		try:
			print '[*] birthday : '+y['birthday'].replace('/','-')
		except KeyError:
			pass
		try:
			print '[*] link : '+y['link']
		except KeyError:
			pass
		try:
			print '[*] Favourite teams : '
			for i in y['favorite_teams']:
				try:
					print ' ~  '+i['name']
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] School : '
			for i in y['education']:
				try:
					print ' ~  '+i['school']['name']
				except KeyError:
					pass
		except KeyError:
			pass
	  else:
		pass

        else:
		print W + ' '
		print '[*] Done '
		main()

#
##########################################################################

##########################################################################
#

if __name__ == '__main__':

	#baliho()
	main()

#
##########################################################################

