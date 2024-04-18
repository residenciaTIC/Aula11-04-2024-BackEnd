# to take the titles of the books at the other pages of the site of
# Livraria da Travessa, i have to inspect if there is a class = 'next',
# take the href using a .get('href'), and then use it as a new url to
# scrape it again

import requests
from bs4 import BeautifulSoup
import cv2
import time

t_in = time.time()  # Marking the initial time of the program
t_wait = 3000  # miliseconds


# url = 'https://www.google.com'
url = 'http://www.travessa.com.br/wpgArtFiltroSeg.aspx?Lanc=S&TipoArtigo=1&TipoPagina=G'

r = requests.get(url)
print('\n\n', r)

soup = BeautifulSoup(r.content, 'html.parser')  # 'lxml'
titles_raw = soup.find_all('a', class_='cover')


'''
for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())

soup.title.string  # it will find the text of a Title header like <title>
soup.a
soup.p
'''


# print(titles_raw)
# print('\n\n\n\n')
# print(titles_raw[0])
# print('\n\n\n\n')


titles_url = []  # list(range(len(titles_raw)))
titles_final = []  # list(range(len(titles_raw)))

# i = 0
for data in titles_raw:
    titles_url.append(data.get('href'))
    titles_final.append(data.get('title'))
    # titles_url[i] = data.get('href')
    # titles_final[i] = data.get('title')
    # print(f'\n\n{titles_url[i]}\n\n{titles_final[i]}\n\n')
    # i += 1


print(f'''

Waiting for {t_wait / 1000} seconds to proceed...''')
cv2.waitKey(t_wait)  # miliseconds

print('\n\n\n\n\n    The URL`s of the new books abvailable at the first page of Livraria da Travessa are:\n\n')
for i in titles_url:
    print(f'''
    {i}''')


print(f'''

Waiting for {t_wait / 1000} seconds to proceed...''')
cv2.waitKey(t_wait)  # miliseconds

print('\n\n\n\n\n    The Titles of the new books abvailable at the first page of Livraria da Travessa are:\n\n')
for j in titles_final:
    print(f'''
    {j}''')
# print(titles_url, '\n\n\n')

t_out = time.time()  # Marking the final time of the program

print(
    f'\n\n\n\nProgram took {t_out - t_in - (2 * t_wait / 1000): .4f} seconds.\n\n')
