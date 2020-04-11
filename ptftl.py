import os
import subprocess
import platform
import sys

# python 2 compatibility
try: input = raw_input
except NameError: pass

# funny random banner
import random
funny = random.sample(["Aliens", "Clowns", "Mr. Robot","Zero Cool", "Goats", "Hackers", "Unicorns"], 1)[0]

def again():
	ptfl()

# color scheme for core
class bcolors:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERL = '\033[4m'
	ENDC = '\033[0m'
	backBlack = '\033[40m'
	backRed = '\033[41m'
	backGreen = '\033[42m'
	backYellow = '\033[43m'
	backBlue = '\033[44m'
	backMagenta = '\033[45m'
	backCyan = '\033[46m'
	backWhite = '\033[47m'

def banner():
	# version information
	grab_version = "0.0.1"

	# banner
	banner = bcolors.RED + r"""

				 ______  __ __    ___
				|      T|  T  T  /  _]
				|      ||  l  | /  [_
				l_j  l_j|  _  |Y    _]
				  |  |  |  |  ||   [_
				  |  |  |  |  ||     T
				  l__j  l__j__jl_____j
	 ____   ___  ____   ______    ___  _____ ______    ___  ____    _____    
	|    \ /  _]|    \ |      |  /  _]/ ___/|      |  /  _]|    \  / ___/    
	|  o  )  [_ |  _  ||      | /  [_(   \_ |      | /  [_ |  D  )(   \_     
	|   _/    _]|  |  ||_|  |_||    _]\__  ||_|  |_||    _]|    /  \__  |    
	|  | |   [_ |  |  |  |  |  |   [_ /  \ |  |  |  |   [_ |    \  /  \ |    
	|  | |     ||  |  |  |  |  |     |\    |  |  |  |     ||  .  \ \    |    
	|__| |_____||__|__|  |__|  |_____| \___|  |__|  |_____||__|\_|  \___|    
																			 
	 _____  ____    ____  ___ ___    ___ __    __   ___   ____   __  _       
	|     ||    \  /    ||   |   |  /  _]  |__|  | /   \ |    \ |  |/ ]      
	|   __||  D  )|  o  || _   _ | /  [_|  |  |  ||     ||  D  )|  ' /       
	|  |_  |    / |     ||  \_/  ||    _]  |  |  ||  O  ||    / |    \       
	|   _] |    \ |  _  ||   |   ||   [_|  `  '  ||     ||    \ |     |      
	|  |   |  .  \|  |  ||   |   ||     |\      / |     ||  .  \|  .  |      
	|__|   |__|\_||__|__||___|___||_____| \_/\_/   \___/ |__|\_||__|\_|      
																			 
	 ______   ___    ___   _          _      ____ _____ ______    ___  ____  
	|      | /   \  /   \ | |        | |    |    / ___/|      |  /  _]|    \ 
	|      ||     ||     || |        | |     |  (   \_ |      | /  [_ |  D  )
	|_|  |_||  O  ||  O  || |___     | |___  |  |\__  ||_|  |_||    _]|    / 
	  |  |  |     ||     ||     |    |     | |  |/  \ |  |  |  |   [_ |    \ 
	  |  |  |     ||     ||     |    |     | |  |\    |  |  |  |     ||  .  \
	  |__|   \___/  \___/ |_____|    |_____||____|\___|  |__|  |_____||__|\_|
																			 
	"""

	banner += bcolors.ENDC + """
			 The"""
	banner += bcolors.BOLD + """ PenTesters """
	banner += bcolors.ENDC + """Framework Lister\n\n"""

	banner += """        		   """ + bcolors.backBlue + \
		"""Version: %s""" % (grab_version) + bcolors.ENDC + "\n"

	banner += bcolors.YELLOW + bcolors.BOLD + """		    Codename: """ + \
		bcolors.BLUE + """List all the Tools""" + "\n"

	banner += """             A project by """ + bcolors.GREEN + bcolors.BOLD + \
		"""Andrew """ + bcolors.RED + """ (aka _agentwhite_) """+ bcolors.ENDC + "\n"

	banner += """		 Written by: """ + bcolors.BOLD + \
		"""Andrew (_agentwhite_)""" + bcolors.ENDC + "\n"
	banner += """		        Twitter: """ + bcolors.BOLD + \
		"""@_agentwhite_""" + bcolors.ENDC + "\n"
	banner += """\n                    """ + bcolors.BOLD + """     All because of """ + \
		bcolors.ENDC + bcolors.BOLD + bcolors.YELLOW + funny + bcolors.ENDC

	banner += """\n                    """ + bcolors.BOLD + """     https://thegibson.xyz
			""" + bcolors.ENDC
	banner += bcolors.BOLD + """\n---------------------------------------------------------------------------------
	""" + bcolors.ENDC + "\n"
	return banner

def ptfl():
	def list_tools():
		modules = []
		tools = []
		installed_modules = 0
		installed_tools = 0

		for x in os.listdir("/pentest/"):
			installed_modules += 1
			print('\t'+ bcolors.RED + x + bcolors.ENDC)
			modules.append(x)
		
		# Check if there is anything installed before we continue
		if installed_modules == 0:
			print("[!] No modules or tools have yet to be installed.")
			print("[i] Try installing some awesome tools from PTF and come back!")
			sys.exit()

		print("There are %s modules installed"% str(installed_modules))

		for i in modules:
			tools = (os.listdir('/pentest/'+i))
			for b in tools:
				installed_tools += 1
				print('\t'+bcolors.RED + i + bcolors.ENDC + "\\"+ bcolors.GREEN + b + bcolors.ENDC)

		print("There are %s tools installed"% str(installed_tools))

	def help_menu():
		print("This is the help menu showing the different list of commands available at the moment")
		print("""
	'h' or 'help' \t Displays this help menu
	'list' or 'list tools' \t Displays all the tools you have installed using The PenTesters Framework
	'exit' or 'shutdown' or 'terminate' \t Exits the PTFL (PenTesters Framework Lister
		""")

	uput = input ("ptfl> ")
	if uput == 'help' or uput == 'h':
		help_menu()
		again()
	elif uput == 'list' or uput == 'list tools' or uput == 'show modules' or uput == 'show':
		print("Listing all the tools you have installed...")
		list_tools()
		again()
	elif uput == 'exit' or uput == 'terminate' or uput == 'shutdown':
		print("Thanks for using The PenTesters Framework Lister")
		print("See you next time!!")
		sys.exit()
	else:
		print(bcolors.RED + "That option is not valid. Check the help menu below..."+ bcolors.ENDC)
		help_menu()
		again()
	#list_tools()

print(banner())
ptfl()
