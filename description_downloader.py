from urllib.request import urlopen
from bs4 import BeautifulSoup

RESPONSE = {
    'title': str,
    'description': str,
}

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, 'lxml')


def scrape_video_data(youtube_video_url):

    soup = make_soup(youtube_video_url).find(id='watch7-content')

    if (soup != None and len(soup.contents) > 1):
        video = RESPONSE

        # get data from tags having `itemprop` attribute
        for tag in soup.find_all(itemprop=True, recursive=False):
            key = tag['itemprop']
            if key == 'name':
                # get video's title
                video['title'] = tag['content']

        # get video description
        description_para = soup.find('p', id='eow-description')
        for br in description_para.find_all('br'):
            br.replace_with('\n')
        video['description'] = description_para.get_text()

        return RESPONSE

    return ({
        'error': 'Video with the ID {} does not exist'.format(id)
    })
