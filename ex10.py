import datetime
myname = 'SAIKUMAR'
myid = 'NCD0518H024'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()



tabby_cat = "\ti'm tabbed in."
persian_cat = "i'm split\non a line"
backslash_cat = "i'm \\ a \\ cat."

fat_cat = """
i'll do a list:
\t* cat food
\t* fishes
\t* catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
