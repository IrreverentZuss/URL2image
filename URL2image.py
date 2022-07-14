#$$$$ Created by Irreverent - 6/21 $$$$#
############### Ver. 1.3 ###############

# Importing libraries.
import clipboard_monitor
import urllib.request
import time
import signal
import sys
import os
from tqdm import tqdm

# Creating class "URL2FhdImage".
class URL2FhdImage():
	# Creating function "__init__" with self as atribute.
	def __init__(self):
			# Defining the usual picture attributes of URLs and desired variables.
			self.newpath = r'.\PicFolder'
			self.MMKw = ['width=640','width=324','width=160','width=79',]
			self.BAw = ['width=1533','width=1289','width=1022','width=859','width=58']
			self.BAh = ['height=450','height=675', 'height=450','height=58']
			self.BAf = ['format=webp']
			# Defining atributes with the desired domain names.
			self.MMK = 'portal.booking-manager.com/wbm2/bmdoc/'
			self.BA = 'imageresizer.yachtsbt.com'
			# Defining final atributes of URLS.
			self.finalWidth = 'width=5000'
			self.finalHeight = 'height=5000'
			self.finalFormat = 'format=jpeg'


	def initialize(self, url):
			while self.stoprunning == False:
				run = URL2FhdImage()
				toDo.append(url)
				print(str(x)+". URL(s) have/has been added to queue for download.")
				#	if time.time() - oldtime > 120 and toDo != '':
				if 
			for x in toDo:
				run.main(x)
				if x == toDo[-1]:
					toDo = [""]
					break
			else:
				print("\n\tWaiting for a URL to be copied...")


	# Print a message.
	print("\n\n\n|*|-Monitoring clipboard for image URL from BoatAround or MMK---2min/time*--|*|")
	# Create funtion "main" with "self" and "url" as variables.
	def main(self, url):
			# If there is no folder "PicFolder" @ the current location of the script
			if not os.path.exists(self.newpath):
				# Create a folder named "PicFolder".
				os.makedirs(self.newpath)
				# Print a message.
				print("\n|~~~|--Folder 'PicFolder' @ current location of script, created--|~~~|\n")
			# If the URL contains the defined domains continue.
			if self.MMK in url:
				# Slice the given URL in order to extract the name of the picture and assign it to the atribute "PicName".
				PicName = url[46:-32]
				# If the image doesn't exist.
				if not os.path.exists(PicName):
					# Print message.
					print("\n\n[*] - ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ - [*]")
					# Print message.
					print("\t[1] - Done Name extraction")
					# For every width in the list "MMK".
					for self.curWidth in self.MMKw:
						# If current width from the list is contained in the URL.
						if self.curWidth in url:
							# Replace the found current width in the URL with the "finalWidth".
							url = url.replace(self.curWidth, self.finalWidth)
							# Print message.
							print("\t[2] - Done Width replacement")
							# Break the for loop.
							break
						# If string "efaultToEmpty=true", exixst into the copied URL.
						if 'defaultToEmpty=true' in url:
							# Replace the found "defaultToEmpty=true" and replace it with "defaultToEmpty=false".
							url = url.replace('defaultToEmpty=true', 'defaultToEmpty=false')
							# Print message.
							print("\t[3] - Done 'defaultToEmpty' replacement")
						# Start the progress bar with some arguments as "t".
						with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, unit_divisor=1024, desc=PicName) as t:	
							# Request the modified URL and save it in the "PicFolder" @ the current location of the script
							# and update about the progress bar according.
							urllib.request.urlretrieve(url, filename="PicFolder/"+PicName, reporthook=t.update_to)
						# Print message.
						print("\n\t[*] - The MMK image saved - [*]\n\n")
					# On failure follow.
				else:
					print("\n\t[$] - Image already exist - [*]\n\n")
			# If the URL contains the defined domain continue.
			elif self.BA in url:
				# Split the "url" and assign the elements to "PicName".
				PicName = url.split('/')
				# Assign "PicName" the fifth element.
				PicName = PicName[5]
				# Cut everything from "?" till the end and assign it to "PicName".
				PicName = PicName[:PicName.index('?'):]
				# Print message.
				print("\n[*] - ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ - [*]")
				# Print message.
				print("\t[1] - Done Name extraction")
				# If the image doesn't exist.
				if not os.path.exists(PicName):
					# For every width in the list "BAw".
					for self.curWidth in self.BAw:
						# If current width in the URL.
						if self.curWidth in url:
							# Replace the found current width with the "finalWidth".
							url = url.replace(self.curWidth, self.finalWidth)
							# Print message.
							print("\t[2] - Done Width replacement")
							# Stop for loop.
							break
					# For every height in the list "BAh".
					for self.curHeight in self.BAh:
						# If current height in the URL.
						if self.curHeight in url:
							# Replace the found current height with the "finalHeight".
							url = url.replace(self.curHeight, self.finalHeight)
							# Print message.
							print("\t[3] - Done Height replacement")
							# Stop for loop.
							break
					# For every format in the list "BAf".
					for self.curFormat in self.BAf:
						if self.curFormat in url:
							# Replace the found current format with the "finalFormat".
							url = url.replace(self.curFormat, self.finalFormat)
							print("\t[4] - Done 'format' replacement")
							# Stop for loop.
							break
					# If string "method=fit", exixst into the copied URL.
					if 'method=fit' in url:
						# Replace the found "method=fit" and replace it with "method=crop".
						url = url.replace('method=fit', 'method=crop')
						# Print message.
						print("\t[5] - Done replacing 'method'")
					# Start the progress bar with some arguments as "t".
					with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, unit_divisor=1024, desc=PicName) as t:	
						# Request the modified URL and save it in the "PicFolder" @ the current location of the script
						# and update about the progress bar according.
						urllib.request.urlretrieve(url, filename="PicFolder/"+PicName, reporthook=t.update_to)
					# Print message.
					print("\n\t[*] - The Boataround image saved - [*]\n\n")
				# On failure follow.
				else:
					# Print message.
					print("\n\t[$] - Image already exist - [$]\n\n")

# Creating class "DownloadProgressBar" with "tqdm" as atrribute.
class DownloadProgressBar(tqdm):
	# Creating function "update_to" with some arguments to share with functions and show on progress bar.
	def update_to(self, b=1, bsize=1, tsize=None):
		# If "tsize" is not empty.
		if tsize is not None:
			# Everytime add tsize to self.total .
			self.total = tsize
		# Update the counter of progress bar with the condition below.
		self.update(b * bsize - self.n)

# If text is copied to the clipboard call from class "URL2FhdImage" function "intialize".
clipboard_monitor.on_text(URL2FhdImage.initialize) 
# Keep thread of listening the clipboard, alive.
