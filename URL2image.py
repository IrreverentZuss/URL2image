#$$$$ Created by Irreverent - 6/21 $$$$#
############### Ver. 1.0 ###############

# Importing libraries.
import urllib.request
import ctypes
import wget
import clipboard_monitor

# Print a message.
print('\n\n\nListen to the copied photo URLS from BoatAround or MMK...\n\n\n')
# Define a new funtion with a "url" as variable.
def URL2FhdImage(url):
		# Defining lists with the usual picture attributes of URLs.
		MMKw = ['width=640','width=324','width=160','width=79',]
		BAw = ['width=1533','width=1022','width=58']			
		BAh = ['height=450','height=58']
		BAf = 'format=webp'
		# Defining atributes "MMKdom", "BAdom" and "doms" with domain names.
		MMK = 'portal.booking-manager.com'
		BA = 'imageresizer.yachtsbt.com'
		doms = MMK or BA
		# Defining lists with final atributes of URLS.
		finalWidth = 'width=5000'
		finalHeight = 'height=5000'
		finalFormat = 'format=jpeg'
		# If the URL contains the defined domains continue.
		if MMK in url:
			# For every current width in the list "MMK".
			for curWidth in MMKw:
				# If the defined domain and the current width from the list are contained in the URL.
				if curWidth and MMK in url:
					# Print message.
					print("I just got the MMK link...\n")
					# Replace the found current width in the URL with the "finalWidth".
					url = url.replace(curWidth, finalWidth)
					# Print message.
					print("***Processing***")
					# Slice the given URL in order to extract the name of the picture and assign it to the atribute "PicName".
					PicName = url[45:-32]
					# Try the following.
					try:
						# Request the modified URL and save it in the "New folder" @ at the current location of the script.
						urllib.request.urlretrieve(url, filename="New folder/"+PicName)
						# Print message.
						print("I just saved the image from MMK...\n")
					# On failure follow.
					except:
						# Print message.
						print("\n****The image already exist****\n")
		elif BA in url:
			# For every current width-height-format in the lists "BAw","BAh" and "BAf".
			for curWidth,curHeight,carFormat in zip(BAw,BAh,BAf):
				# If the defined domain and the current width-height-format from the lists are contained in the URL.
				if BA and curWidth and curHeight and curFormat in url:
					# Print message.
					print("I just got the link BoatAround...\n")
					# Replace the found current width-height-format with the "finalWidth"-"finalHeight"-"finalForamt".
					url = url.replace(curWidth, finalWidth) & url.replace(curHeight, finalHeight) & url.replace(curFormat, finalFormat)
					# Print message.
					print("***Processing***")
					# Slice the given URL in order to extract the name of the picture and assign it to the atribute "PicName".
					PicName = url[75:-47]
					# Try the following.
					try:
						# Request the modified URL and save it in the "New folder" @ the current location of the script.
						urllib.request.urlretrieve(url, filename="New folder/"+PicName)
						# Print message.
						print("I just saved the image from Boataround...")
					# On failure follow.
					except:
						# Print message
						print("\n****The image already exist****\n")
		# If the URL does not contain the propair URL to download picture.	
		else:
			# Print message.
			print("\n***Waiting for a URL from Boataround or MMK***\n")
# If something is copied to the clipboard call function definition "URL2FhdImage".
clipboard_monitor.on_text(URL2FhdImage)
# Keep the thread of listing the clipboard, alive.
clipboard_monitor.wait()
