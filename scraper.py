import requests


url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=202101&CourseNumber=cis189'
response = requests.get(url)
html = response.content
f = open("requestResult.txt","w+")
f.writelines(str(html))
f.close()
