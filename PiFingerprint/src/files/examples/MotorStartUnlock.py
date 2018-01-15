delay = 1
steps = 250
def motor_start(delay,step):
	import RPi.GPIO as GPIO
	import time
	print 'Motors Starting...'
#enable_pin = 6,13,19,26 # This might be able to go? 
 
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	#in order of firing magnets
	coil_pin_4 = 26 # Yellow
	coil_pin_3 = 19 # Orange
	coil_pin_2 = 13 # Red
	coil_pin_1 = 6 # Brown
 
	StepCount = 8
	Seq = range(0, StepCount)
	#my revision 
	Seq[0] = [0,0,0,1]
	Seq[1] = [0,0,1,1]
	Seq[2] = [0,0,1,0]
	Seq[3] = [0,1,1,0]
	Seq[4] = [0,1,0,0]
	Seq[5] = [1,1,0,0]
	Seq[6] = [1,0,0,0]
	Seq[7] = [1,0,0,1]

	#Original
	#Seq[0] = [0,1,0,0]
	#Seq[1] = [0,1,0,1]
	#Seq[2] = [0,0,0,1]
	#Seq[3] = [1,0,0,1]
	#Seq[4] = [1,0,0,0]
	#Seq[5] = [1,0,1,0]
	#Seq[6] = [0,0,1,0]
	#Seq[7] = [0,1,1,0]
 
	#GPIO.setup(enable_pin, GPIO.OUT)
	GPIO.setup(coil_pin_4, GPIO.OUT)
	GPIO.setup(coil_pin_2, GPIO.OUT)
	GPIO.setup(coil_pin_3, GPIO.OUT)
	GPIO.setup(coil_pin_1, GPIO.OUT)
	#GPIO.output(enable_pin, 1)
 
	def setStep(w1, w2, w3, w4):
		#4321 - firing order
		GPIO.output(coil_pin_4, w4)
		GPIO.output(coil_pin_2, w2)
		GPIO.output(coil_pin_3, w3)
		GPIO.output(coil_pin_1, w1)
    
	def forward(delay, steps):
		for i in range(steps):
			for j in range(StepCount):
				setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
				time.sleep(delay)
		print 'Unlocked'
 
	def backwards(delay, steps):
		for i in range(steps):
			for j in reversed(range(StepCount)):
				setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
				time.sleep(delay)
		print 'Locked'

#	delay = raw_input("Time Delay (ms)?")
#	steps = raw_input("How many steps forward? ")
	forward(int(delay) / 1000.0, int(steps))
#	steps = raw_input("How many steps backwards? ")
#	backwards(int(delay) / 1000.0, int(steps))
 
#def main(delay,steps):
	# Motor step and delay values
	#perform motor_start
	#motor_start(delay,steps)

#if __name__ == '__main__':
	#main(delay,steps)
