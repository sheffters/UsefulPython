import sys
import threading
import time
import thread
import multiprocessing
import os
from random import randint

# This provides thread-safe print screen.
# It could also be tweaked to print to file etc.
# Nifty.

# Totally robbed from http://stackoverflow.com/questions/3029816/how-do-i-get-a-thread-safe-print-in-python-2-6 and then mashed up a bit to test.

class ThreadSafePrint(object):
	def __init__(self, f):
		self.f = f
		self.lock = threading.RLock()
		self.nesting = 0

	def _getlock(self):
		self.lock.acquire()
		self.nesting += 1

	def _droplock(self):
		nesting = self.nesting
		self.nesting = 0
		for i in range(nesting):
			self.lock.release()

	def __getattr__(self, name):
		if name == 'softspace':
			return tls.softspace
		else:
			raise AttributeError(name)

	def __setattr__(self, name, value):
		if name == 'softspace':
			tls.softspace = value
		else:
			return object.__setattr__(self, name, value)

	def write(self, data):
		self._getlock()
		self.f.write(data)
		if data == '\n':
			self._droplock()

sys.stdout = ThreadSafePrint(sys.stdout)


# Some example shinnanigans below.


#    Create generic code for each thread.
def GenericThreadCode(name):
	
	counter = 0
	
	while 1 < 2:
		
		counter_print = '{:>10}'.format(counter)
		
		print str(name) + " is smegtastic. " + str(counter_print) + " iterations so far and no thread mess!"
		
		counter = int(counter) + 1
		
		time.sleep(randint(0,2))



# Kick the threads off

cpu_count = multiprocessing.cpu_count()

print "We have " + str(cpu_count) + " CPU threads available."

cpu_count = cpu_count - 1

print "   Will keep a thread free for system, using " + str(cpu_count) + " threads."

time.sleep(1)

try:
	
	counter = 0
	
	while int(counter) < int(cpu_count):
		
		thread_name = 'Thread ' + str("{0:03d}".format(counter))
		
		thread.start_new_thread( GenericThreadCode, (thread_name, ) )
		
		counter = int(counter) + 1

except:
	
	print "Bugger, unable to start thread."

while 1:
	
	pass