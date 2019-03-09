import threading
from queue import Queue
import timestamp as timestamp
from spider import Spider
from Domain import *
from DataFiles import *


# x = "http://www.wikipedia.org"
# x = "http://www.wallpaperscraft.com"
x = "https://unsplash.com/search/photos/wallpaper"
# x = "https://unsplash.com/search/photos/wallpaper"
# x = "https://www.facebook.com"
# x = "https://wallpaperscraft.com/wallpaper/bubbles_circles_dark_136091"
# x = "https://wallpapers.wallhaven.cc"
# x = "https://www.google.com/search?tbm=isch&q=tigger"

PROJECT_NAME = str(timestamp())
print(PROJECT_NAME)
HOMEPAGE = x
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' Links in the queue')
        create_jobs()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
        queue.join()
        crawl()


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


create_workers()
crawl()