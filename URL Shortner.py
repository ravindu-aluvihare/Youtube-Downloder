import pyshorteners

url = input('Enter the URL: ')

def shortenurl(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url) 

short_url = shortenurl(url)

print(f'Short URL: {short_url}')
