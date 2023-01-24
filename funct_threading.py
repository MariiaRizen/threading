from PIL import Image
import requests
from threading import Thread
from time import time
from functools import wraps


def time_function(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print(f.__name__ + " " + "took" + " " + str((end - start) * 100000) + 'ms')
        return result
    return wrapper


def cropp_image():
    image_path = r'C:\Users\Admin\Downloads\img_flow.jpg'
    image = Image.open(image_path)
    small_image = image.resize((500, 500))
    small_image.save('image.jpg')


def make_request():
    requests.get('https://www.python.org')


@time_function
def sync_make_request():
    for i in range(5):
        make_request()

@time_function
def async_make_request():
    # Thread(target=make_request)
    # Thread(target=make_request)
    # Thread(target=make_request)
    # Thread(target=make_request)
    # Thread(target=make_request)
    threads = list()
    for index in range(5):
        x = Thread(target=make_request)
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        thread.join()


@time_function
def sync_cropp_image():
    for i in range(5):
        cropp_image()


@time_function
def async_cropp_image():
    # Thread(target=cropp_image)
    # Thread(target=cropp_image)
    # Thread(target=cropp_image)
    # Thread(target=cropp_image)
    # Thread(target=cropp_image)
    threads = list()
    for index in range(5):
        x = Thread(target=make_request)
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        thread.join()


if __name__ == '__main__':
    sync_make_request()
    async_make_request()
    sync_cropp_image()
    async_cropp_image()
    #синхронна функція із обробкою зображення виконується швидше, а у виконанні запитів навпаки