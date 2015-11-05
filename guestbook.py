import datetime
import json

# populate a list containing all the entry data
with open("guestbook.json", "r") as f:
    data = json.loads(f.read())

print "How many previous entries would you like to view?"
entries = int(raw_input(" - "))
list_len = len(data)

if list_len == 0:
    print "Sorry, there are no entries in the guest book."
elif list_len < entries:
    print "Sorry, there aren't that many entries."
    print "Here are all the previous entries."
    for x in data:
        print x[0], " left a message on %s - %s - %s." % (x[1], x[2], x[3])
        print "The message was %s." % x[4]
else:
    for x in range(0, entries):
        y = data[len(data) - 1 - x]
        print y[0], " left a message on %s - %s - %s." % (y[1], y[2], y[3])
        print "The message was %s." % y[4]

# take input for the name and message
print "Please enter your name for the guestbook."
name = raw_input(" -- ")
print "Please enter a message for the guestbook."
message = raw_input(" -- ")

# format the date
date_string = str(datetime.datetime.today())
year = date_string[0:4]
month = date_string[5:7]
day = date_string[8:10]

# save the new entry
with open("guestbook.json", "w") as f:
    new_entry = [name, month, day, year, message]
    data.append(new_entry)
    f.write(json.dumps(data))

print "Your message is : \" ",message," \" "
print "It was left on ", month, "-", day, "-", year
print "Goodbye!"