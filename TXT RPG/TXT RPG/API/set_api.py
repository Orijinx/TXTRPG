import urllib.request
import requests

#webUrl  = urllib.request.urlopen('http://f91091jy.beget.tech/set_api.php?var1=5&var2=8')

#webURL = urllib.request.urlopen('http://f91091jy.beget.tech/setapi.php?submit=Avemaria')
#print ("result code: " + str(webUrl.getcode()))

#g= requests.post('http://f91091jy.beget.tech/setapi.php', data = {'var1':'228322'})
response = requests.get('http://f91091jy.beget.tech/setapi.php', params={'var1':'228322'})
print(response.url)
print(response.status_code)