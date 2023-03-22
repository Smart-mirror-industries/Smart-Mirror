import requests

#Canvas Export Link
url = 'https://erau.instructure.com/feeds/calendars/user_3tuGhpDjBVOJLZ6wPiMKgXWa0vlyU1o6GoAMeycj.ics'

r = requests.get(url) # create HTTP response object
  
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("test.ics",'wb') as f:
  
    # Saving received content as a png file in
    # binary format
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)
    print("test")