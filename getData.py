import os
import requests

# Prepare directory
directory = "download"
if not os.path.exists(directory):
    os.makedirs(directory)


# Get captcha
def leftpad(i, n):
    n_digit = len(str(i))
    if n_digit > n:
        print("Too many digits!")
        exit()
    s = ""
    for j in range(n - n_digit):
        s += '0'
    s += str(i)
    return s


def fetch_captcha(n):
    url = "https://w6.ab.ust.hk/fbs_user/Captcha.jpg"
    for i in range(n):
        r = requests.get(url)
        open(os.path.join(os.path.abspath(directory), "z{}.png".format(leftpad(i, 3))), 'wb').write(r.content)
    print("Downloaded {} image(s) to {}.".format(n, os.path.abspath(directory)))


fetch_captcha(10)
