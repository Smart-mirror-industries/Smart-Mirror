import requests
from ics import Calendar, Event

#Canvas Export Link
url = 'https://erau.instructure.com/feeds/calendars/user_3tuGhpDjBVOJLZ6wPiMKgXWa0vlyU1o6GoAMeycj.ics'

r = requests.get(url) # Get Calendar File


c = Calendar(r.text)  # Read calender file 

c

c.events


# send a HTTP request to the server and save
# the HTTP response in a response object called r
for i in range(10):
    e = list(c.timeline)[i]
    print("Event '{}' started {}".format(e.name, e._end_time))
with open("test.ics",'wb') as f:
  
    # Saving received content as a png file in
    # binary format
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)
    print("test")