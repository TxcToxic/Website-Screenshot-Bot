# Made with <3 again!
# ! -TOXIC-#1835 !

import os
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def print2(text: str):
    print(f"\n{text}\n")


def logoPrint():
    os.system("clear || cls")
    print("""██╗    ██╗███████╗██████╗  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
██║    ██║██╔════╝██╔══██╗██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝██║     ███████║█████╗  ██║     █████╔╝ 
██║███╗██║██╔══╝  ██╔══██╗██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
╚███╔███╔╝███████╗██████╔╝╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
                         by CFT-Development                       """)


def cWeb(url: str, path="./", randomend=True):
    options = webdriver.ChromeOptions()
    # use the 2 options below if you want to completely DON'T show the Chrome window.
    # if you use the options below disable driver.minimize_window()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    options.add_argument("--mute-audio")  # leave this activated, who knows the site can be a jump-scare
    # options.add_argument("--disable-web-security")  # Use this on your own risk or use it on a VM
    # options.add_argument("--disable-site-isolation-trials")  # Use this on your own risk or use it on a VM
    driver = webdriver.Chrome(r"./bin/chromedriver.exe", chrome_options=options)
    try:
        driver.get('{}'.format(url) if "http" in url else 'http://{}'.format(url))
    except:
        return print2("Cannot open page!")
    driver.minimize_window()  # look in line 29 & 30
    sleep(1.2)
    if "youtube" in driver.current_url:
        try:
            driver.find_element(By.XPATH,
                                "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div").click()
        except:
            sleep(2)
            try:
                driver.find_element(By.XPATH,
                                    "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div").click()
            except:
                pass
            print2("skip cookie acception failed!")
        sleep(2.5)  # Youtube needs more time to load the videos and show to cookie acception
    if "pnrtscr" in driver.current_url:
        # it's the one website if you know ;) ( https://pnrtscr.com/fep8be )
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]").click()
        except:
            sleep(2)
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]").click()
            except:
                pass
            print2("skip acception failed!")
    if randomend:
        nEnd = "".join(random.choice(string.digits) for _ in range(4))
    else:
        nEnd = ""
    driver.get_screenshot_as_file(f"{path}screenshot{'_' + nEnd if not nEnd == '' else ''}.png")
    driver.quit()


if __name__ == "__main__":
    os.system("title WebCheck   by -TOXIC-#1835")
    logoPrint()
    while True:
        link = input("> ")
        if link.casefold() in ("exit", "quit", "close"):
            quit()
        elif link.casefold() in ("help", "info"):
            print2("Commands: help (info), exit (quit and close),\n"
                   "          clear (cls and purge) or simply enter a link!")
        elif link.casefold() in ("clear", "cls", "purge"):
            logoPrint()
        else:
            cWeb(url=link, path="./pics/")
            # you can also add path (string) (where it get saved)
            # or randomend (bool) (if you want more than one screenshot)
