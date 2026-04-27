import webbrowser
import urllib.parse

params = {
    'action': 'TEMPLATE',
    'text': 'test event',
    'dates': '20260425T020000Z/20260425T030000Z',
    'ctz': 'Asia/Dhaka',
    'details': 'Event created via CLI'
}

url = 'https://calendar.google.com/calendar/render?' + urllib.parse.urlencode(params)
print('Opening:', url)
webbrowser.open(url)
