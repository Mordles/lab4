#!/usr/bin/python37all

import json
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
radio_button = form.getvalue("option")
slider_position = form.getvalue("slider")
data = {"option":radio_button, "slider":slider_position}
with open('selected_led.txt', 'w') as f:
  json.dump(data,f)

print('Content-type:text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/select_led.py" method="POST">')
print('<input type="radio" name="option" value="1"> LED 1 <br>')
print('<input type="radio" name="option" value="2"> LED 2 <br>')
print('<input type="radio" name="option" value="3"> LED 3 <br>')
print('<input type="submit" value="Submit"> <br>')
print('<input type="range" name="slider" min="0" max="100" value="%s"><br>' % slider_position)
print('<input type="submit" value="Change selected LED brightness">')
print('</form>')
print('Brightness = %s' % slider_position)
print('</html>')  
