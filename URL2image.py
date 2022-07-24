# |^^^| Created: 6/22' ^^^ Last Updated: 7/22 ^^^ by: Irreverent |^^^|
###############  Ver. 1.5 ###############

#  Importing libraries.
import clipboard_monitor
import urllib.request
import os
from tqdm import tqdm
from pynput import keyboard
from rich import print, pretty

#  Creating class 'URL2FHDimage'.
class URL2FHDimage():
	#  Creating '__init__' with 'self'.
	def __init__(self):
			#  Defining the usual picture attributes of URLs and desired variables.
			self.newpath = r'.\PicFolder'
			self.MMKw = ['width=640','width=324','width=160','width=79',]
			self.BAw = ['width=1533','width=1289','width=1022','width=859','width=58']
			self.BAh = ['height=450','height=675', 'height=450','height=58']
			self.BAf = ['format=webp']
			self.toDo = ['']
			#  Defining atributes with the desired domain names.
			self.MMK = 'portal.booking-manager.com/wbm2/bmdoc/'
			self.BA = 'imageresizer.yachtsbt.com'
			#  Defining final atributes of URLS.
			self.finalWidth = 'width=5000'
			self.finalHeight = 'height=5000'
			self.finalFormat = 'format=jpeg'


	#  Print messages.
	print('\n\n|@|\t|~|\t|@|\t|~|\t|@|\t|~|\t|@|\t|~|\t|@|\n')
	print('\tStart copying img URLs from BA or MMK.')
	print('!nf0!\t1) "ctrl+g" to save the images from the copied URL(s)\t!nf0!')
	print('!nf0!\t2) "ctrl+e" to exit\t\t\t\t\t!nf0!\n\n\n')

	#  Creating 'on_press' to deal with the pressed buttons.
	def press_on(key):
			#  Using of try/except.
			try:
				#  Do nothing.
				pass
			#  Catch the error - if there is one.
			except AttributeError:
				#  Print the message with the keystroke(s).
				print('\n\n\t\t|***| Special key {0} pressed'.format(key))


	# Creating 'press_off' to deal with the release of keystrokes.
	def press_off(key):
			Key4Save = keyboard.HotKey(keyboard.HotKey.parse('^G'))
			Key4Exit = keyboard.HotKey(keyboard.HotKey.parse('^E'))
			#  If there is a keystroke similar to the 'self.Key4Save'.
			if key == Key4Save:
				# Start 'execute()'
				self.execute()
			elif key == Key4Exit:
				print('\n\n\t\t-----g00b1e hum4n-----')
				#  Wait for 2 sec.
				time.wait(2)
				#  Exit program
				exit()
			# For everything else than the two keystroke combinations above, do nothing.
			else:
				#  Do nothing.
				pass


	#  Creating function 'initialize' with 'self' and 'url' as atribute.
	def initialize(self, url):
			if self.MMK or self.BA in url:
				self.toDo.append(url)
				print('\n\t| ' + len(self.toDo) + ' |\tURL(s) has/have been added to queue for download.')
			else:
				print('!! -- The link has been already queued -- !!')


	def execute(self):
			if self.toDo != ['']:
				for x in self.toDo:
					if len(self.toDo(x)) < len(self.todo):
						new.main(x)
					else:
						print ('\n\t\t--|@|--\tDone saving images..\t--|@|--')
						self.toDo = ['']
					break
			else:
				print('\n\n\t\tKopiare URLs giati eides ti ekane o theos stous protoplastous ;)\n\n')


	#  Funtion 'main' with 'self' and 'url' as variables.
	def main(self, url):
			#  If there is no folder 'PicFolder' @ the current location of the script
			if not os.path.exists(self.newpath):
				#  Create a folder named 'PicFolder'.
				os.makedirs(self.newpath)
				#  Print a message.
				print('\n|~~~|--Folder "PicFolder" @ current location of script, created--|~~~|\n')
			#  If the URL contains the defined domains continue.
			if self.MMK in url:
				#  Split the copied URL by character '?' and assign it to 'PicName'.
				PicName = url.split('?')
				#  Set 'PicName' the first segment from the split.
				PicName = PicName[0]
				#  Slice the given URL in order to extract the name of the picture and assign it to the atribute 'PicName'.
				PicName = PicName[46:]
				#  If the image doesn't exist.
				if not os.path.exists('.\\PicFolder\\' + PicName):
					#  Print message.
					print('\n\n[*] - ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ - [*]')
					#  Print message.
					print('\t[1] - Done Name extraction')
					#  For every width in the list 'MMK'.
					for self.curWidth in self.MMKw:
						#  If current width from the list is contained in the URL.
						if self.curWidth in url:
							#  Replace the found current width in the URL with the 'finalWidth'.
							url = url.replace(self.curWidth, self.finalWidth)
							#  Print message.
							print('\t[2] - Done Width replacement')
							#  Break the for loop.
							break
					#  If string 'efaultToEmpty=true', exixst into the copied URL.
					if 'defaultToEmpty=true' in url:
						#  Replace the found 'defaultToEmpty=true' and replace it with 'defaultToEmpty=false'.
						url = url.replace('defaultToEmpty=true', 'defaultToEmpty=false')
						#  Print message.
						print('\t[3] - Done "defaultToEmpty" replacement')
					#  Start the progress bar with some arguments as 't'.
					with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, unit_divisor=1024, desc=PicName) as t:	
						#  Request the modified URL and save it in the 'PicFolder' @ the current location of the script
						#  and update about the progress bar according.
						urllib.request.urlretrieve(url, filename='PicFolder/'+PicName, reporthook=t.update_to)
					#  Print message.
					print('\n\t[*] - The MMK image saved - [*]\n\n')
				#  On failure follow.
				else:
					print('\n\t[$] - Image already exist - [$]\n\n')
			#  If the URL contains the defined domain continue.
			elif self.BA in url:
				#  Split the 'url' and assign the elements to 'PicName'.
				PicName = url.split('/')
				#  Assign 'PicName' the fifth element.
				PicName = PicName[5]
				#  Cut everything from '?' till the end and assign it to 'PicName'.
				PicName = PicName[:PicName.index('?'):]
				#  If the image doesn't exist.
				if not os.path.exists('.\\PicFolder\\' + PicName):
					#  Print message.
					print('\n[*] - ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ - [*]')
					#  Print message.
					print('\t[1] - Done Name extraction')
					#  For every width in the list 'BAw'.
					for self.curWidth in self.BAw:
						#  If current width in the URL.
						if self.curWidth in url:
							#  Replace the found current width with the 'finalWidth'.
							url = url.replace(self.curWidth, self.finalWidth)
							#  Print message.
							print('\t[2] - Done Width replacement')
							#  Stop for loop.
							break
					#  For every height in the list 'BAh'.
					for self.curHeight in self.BAh:
						#  If current height in the URL.
						if self.curHeight in url:
							#  Replace the found current height with the 'finalHeight'.
							url = url.replace(self.curHeight, self.finalHeight)
							#  Print message.
							print('\t[3] - Done Height replacement')
							#  Stop for loop.
							break
					#  For every format in the list 'BAf'.
					for self.curFormat in self.BAf:
						#  If current format in the URL.
						if self.curFormat in url:
							#  Replace the found current format with the 'finalFormat'.
							url = url.replace(self.curFormat, self.finalFormat)
							#  Print message.
							print('\t[4] - Done "format" replacement')
							#  Stop for loop.
							break
					#  If string 'method=fit', exixst into the copied URL.
					if 'method=fit' in url:
						#  Replace the found 'method=fit' and replace it with 'method=crop'.
						url = url.replace('method=fit', 'method=crop')
						#  Print message.
						print('\t[5] - Done replacing "method"')
					#  Start the progress bar with some arguments as 't'.
					with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, unit_divisor=1024, desc=PicName) as t:	
						#  Request the modified URL and save it in the 'PicFolder' @ the current location of the script
						#  and update about the progress bar according.
						urllib.request.urlretrieve(url, filename='PicFolder/'+PicName, reporthook=t.update_to)
					#  Print message.
					print('\n\t[*] - The Boataround image saved - [*]\n\n')
				#  On failure follow.
				else:
					#  Print message.
					print('\n\t[$] - Image already exist - [$]\n\n')


#  Creating class 'DownloadProgressBar' with 'tqdm' as atrribute.
class DownloadProgressBar(tqdm):
	#  Creating function 'update_to' with some arguments to share with functions and show on progress bar.
	def update_to(self, b=1, bsize=1, tsize=None):
		#  If 'tsize' is not empty.
		if tsize is not None:
			#  Everytime add tsize to self.total .
			self.total = tsize
		#  Update the counter of progress bar with the condition below.
		self.update(b * bsize - self.n)


#  Make a new instance of class 'URL2FHDimage'.
run = URL2FHDimage()
pretty.install()
try:
	#  If text is copied to the clipboard call 'intialize' from 'URL2FHDimage'.
	clipboard_monitor.on_text(run.initialize)
	#clipboard_monitor.on_text(run.main)
#  Catch errors.
except Exception as E:
	#  Print errors.
	print('\n\n\n\t\tAn error occured and it is as follows: \n\t\t'+ E)
#  Keep the script alive for a new clipboard copy.
clipboard_monitor.wait()
#  Join the pressed and released combination of keystrokes.
with keyboard.Listener(on_press=press_on, on_release=press_off) as listener:
	listener.join()
