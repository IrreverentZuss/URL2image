#$$$$ Created by Irreverent - 6/21 $$$$#
############### Ver. 1.0 ###############

# Importing libraries.
import clipboard_monitor
import urllib.request


# Print a message.
print('\n\n\nListen to the copied photo / URLS from BoatAround or MMK...\n\n\n')
# Define a new funtion with a "url" as variable.
def URL2FhdImage(url):
		# Defining lists with the usual picture attributes of URLs.
		MMKw = ['width=640','width=324','width=160','width=79',]
		BAw = ['width=1533','width=1289','width=1022','width=859','width=58']			
		BAh = ['height=450','height=675', 'height=450','height=58']
		BAf = ['format=webp']
		# Defining atributes "MMKdom", "BAdom" and "doms" with domain names.
		MMK = 'portal.booking-manager.com/wbm2/bmdoc/'
		BA = 'imageresizer.yachtsbt.com'
		doms = MMK or BA
		# Defining lists with final atributes of URLS.
		finalWidth = 'width=5000'
		finalHeight = 'height=5000'
		finalFormat = 'format=jpeg'
		# If the URL contains the defined domains continue.
		if MMK in url:
			# Print message.
			print("\n\nI just got the MMK link...\n")
			# For every width in the list "MMK".
			for curWidth in MMKw:
				# If current width from the list is contained in the URL.
				if curWidth in url:
					# Replace the found current width in the URL with the "finalWidth".
					url = url.replace(curWidth, finalWidth)
					# Print message.
					print("***Done replacing width***")
					# Break the for loop.
					break
			# If string "efaultToEmpty=true", exixst into the copied URL.
			if 'defaultToEmpty=true' in url:
				# Replace the found "defaultToEmpty=true" and replace it with "defaultToEmpty=false".
				url = url.replace('defaultToEmpty=true', 'defaultToEmpty=false')
				# Print message.
				print("***Done replacing 'defaultToEmpty'***")
			# Slice the given URL in order to extract the name of the picture and assign it to the atribute "PicName".
			PicName = url[46:-32]
			# Print message.
			print("***Name copied:  " + PicName + "  ***")
			# Print message.
			print("***Processing done - URL to be downloaded:\n" + url)
			# Try the following.
			try:
				# Request the modified URL and save it in the "New folder" @ the current location of the script.
				urllib.request.urlretrieve(url, filename="New folder/"+PicName)
				# Print message.
				print("              ****\nI just saved the image from MMK...\n              ****\n\n")
			# On failure follow.
			except:
				for i in range(1, 2):
					# Set the number of i plus the PicName in order to be able to save it.
					PicName = str(i) + PicName
					# Request the modified URL and save it in the "New folder" @ the current location of the script.
					urllib.request.urlretrieve(url, filename="New folder/"+PicName)
					# Print message
					print("***The image already exist, that's why I download it by name: "+PicName)
					# Stop for loop.
					break
		elif BA in url:
			# Print message.
			print("\n\nI just got the BoatAround link...\n")
			# For every width in the list "BAw".
			for curWidth in BAw:
				# If current width in the URL.
				if curWidth in url:
					# Replace the found current width with the "finalWidth".
					url = url.replace(curWidth, finalWidth)
					# Print message.
					print("***Done replacing width...")
					# Stop for loop.
					break
			# For every height in the list "BAh".
			for curHeight in BAh:
				# If current height in the URL.
				if curHeight in url:
					# Replace the found current height with the "finalHeight".
					url = url.replace(curHeight, finalHeight)
					# Print message.
					print("***Done replacing height...")
					# Stop for loop.
					break
			# For every format in the list "BAf".
			for curFormat in BAf:
				if curFormat in url:
					# Replace the found current format with the "finalFormat".
					url = url.replace(curFormat, finalFormat)
					print("***Done replacing format...***")
					# Stop for loop.
					break
			# If string "method=fit", exixst into the copied URL.
			if 'method=fit' in url:
				# Replace the found "method=fit" and replace it with "method=crop".
				url = url.replace('method=fit', 'method=crop')
				# Print message.
				print("***Done replacing 'method'***")
			# Slice the given URL in order to extract the name of the picture and assign it to the atribute "PicName".
			PicName = url[63:-47]
			# Print message.
			print("***Name copied:  " + PicName)
			# Print message.
			print("*Processing Done - URL to be downloaded:\n" + url[-46:])
			# Try the following.
			try:
				# Request the modified URL and save it in the "New folder" @ the current location of the script.
				urllib.request.urlretrieve(url, filename="New folder/"+PicName)
				# Print message.
				print("                ****\nI just saved the image from Boataround...\n                ****\n\n")
				# Stop for loop.
			# On failure follow.
			except:
				for i in range(1, 2):
					# Set the number of i plus the PicName in order to be able to save it.
					PicName = str(i) + PicName
					# Request the modified URL and save it in the "New folder" @ the current location of the script.
					urllib.request.urlretrieve(url, filename="New folder/"+PicName)
					# Print message
					print("***The image already exist, that's why I download it by name: "+PicName)
					# Stop for loop.
					break
# If text is copied to the clipboard call function definition "URL2FhdImage".
clipboard_monitor.on_text(URL2FhdImage)
# Keep the thread of listing the clipboard, alive.
clipboard_monitor.wait()
