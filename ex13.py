import datetime
myname = 'SAIKUMAR'
myid = 'NCD0518H024'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()


from sys import argv

script, first, second, third = argv

print "the script is called:", script
print "your first variable is:", first
print "your second variable is:", second
print "your third variable is:", third
