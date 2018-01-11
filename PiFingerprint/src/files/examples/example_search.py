#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""
def fingerprintread(inLoop,Locked):
	## Tries to initialize the sensor
	try:
		f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

		if ( f.verifyPassword() == False ):
			raise ValueError('The given fingerprint sensor password is wrong!')

	except Exception as e:
		print('The fingerprint sensor could not be initialized!')
		print('Exception message: ' + str(e))
		exit(1)

	## Gets some sensor information
	print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

	## Tries to search the finger and calculate hash
	## Start loop here
	##while (inLoop == 0):
	##print 'Loop start'
	try:
		print('Waiting for finger...')

		## Wait that finger is read
		while ( f.readImage() == False ):
			pass

		## Converts read image to characteristics and stores it in charbuffer 1
		f.convertImage(0x01)

		## Searchs template
		result = f.searchTemplate()

		positionNumber = result[0]
		accuracyScore = result[1]

		if ( positionNumber == -1 ):
			print('No match found!')
			##exit(0)
		else:
			print('Found template at position #' + str(positionNumber))
			print('The accuracy score is: ' + str(accuracyScore))
			#Test for locked door variable
			#print('The door is: %s' % Locked)
			
			if (Locked == True):
				#Unlock
				Locked = False
				print 'Unlocked the door'
				fingerprintread(inLoop,Locked)
			
			if (Locked == False):
				#Lock
				Locked = True
				print 'Locked the door'
				fingerprintread(inLoop,Locked)
			
		## OPTIONAL stuff
		##

		## Loads the found template to charbuffer 1
		f.loadTemplate(positionNumber, 0x01)

		## Downloads the characteristics of template loaded in charbuffer 1
		characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

		## Hashes characteristics of template
		print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

	except Exception as e:
		print('Operation failed!')
		print('Exception message: ' + str(e))
		##exit(1)
		
def UnlockDoor(inLoop,Locked):
	#Call motor function for unlocking
	MotorStart.motor_start()
	#Door will now be unlocked
	print 'Door is unlocked'
	#Set the Locked var to False - as the door is unlocked
	Locked = False
	#Exit loop
	inLoop = 1
	#Call function again with the hope of skipping this function
	fingerprintread(inLoop,Locked)
	
def LockDoor(inLoop,Locked):
	#Call motor function for locking
	MotorStart.motor_start()
	#Door will now be locked
	print 'Door is locked'
	#Set the Locked var to True - as the door is now locked
	Locked = True

if __name__ == '__main__':	
	import hashlib
	import MotorStart
	from pyfingerprint.pyfingerprint import PyFingerprint
	## Global Var for loop here
	inLoop = 0
	## Locked/Unlocked identification var
	Locked = True

	## Search for a finger
	##

	#Start fingerprint search
	fingerprintread(inLoop,Locked)
