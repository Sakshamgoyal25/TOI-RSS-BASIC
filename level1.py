from bs4 import BeautifulSoup
import requests
from time import sleep

print("program started")
s1={ 
	'india' : 'https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms' , 
	'world' : 'https://timesofindia.indiatimes.com/rssfeeds/296589292.cms' , 
	'business' : 'https://timesofindia.indiatimes.com/rssfeeds/1898055.cms', 
	'sports' : 'https://timesofindia.indiatimes.com/rssfeeds/4719148.cms', 
	'Science' : 'https://timesofindia.indiatimes.com/rssfeeds/-2128672765.cms'}

for  key, value in s1.items():
 	print(key)
 	
get_cat=str(input("Enter the category of the News you want\n"))
result=requests.get(s1[get_cat])
sleep(1)
print("1st link fetched - rss feed")

result.encoding = result.apparent_encoding
soup = BeautifulSoup(result.text, 'xml')
# print (result.text)

s2 = dict()
i=1
for item in soup.find_all('item'):
	print("fetching item - "+str(i))
	link=item.link.text
	title=item.title.text
	desc=item.description.text
	if i<=2:
		s3 = dict()
		s3['title'] = title
		s3['description'] = desc
		s3['link'] = link
		s2[i]= s3
	else:
		break
	i=i+1

# print("1st link fetched - rss feed")
#print(s2)
for i in range(1,3):
	print(i)
	print(s2[i]['title'])
get_titno=int(input("Enter the number corresponding to title you want\n"))

print ("Your title is:")
print(s2[get_titno]['title'])


fresult=requests.get(s2[get_titno]['link'])
fsoup = BeautifulSoup(fresult.text, 'html.parser')

print(fsoup.find('div',class_='section1').text)
	
	






	




	