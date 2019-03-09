import urllib.request


def download(url):
    a = url.split('?')
    c = a[0].split('/')
    name = c[-1] + '.jpg'
    print(name)
    b = url.split('"')
    urllib.request.urlretrieve(b[-2], name)
    print(name + 'downloaded \n\n')

