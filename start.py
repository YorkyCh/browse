from selenium import webdriver
import os
import time
from pynput import keyboard
from selenium.common.exceptions import NoSuchWindowException


def start(name):
    session_file = f"./sessions/{name}.csv"
    driver = None
    open_urls = set()
    try:
        if not os.path.exists(session_file):
            print(f"Error: The '{name}' file does not exist.")
            return
        with open(session_file, "r") as f:
            lines = [line.strip() for line in f.readlines()]

        driver = webdriver.Chrome()
        for i, url in enumerate(lines):
            if i == 0:
                driver.get(url)
            else:
                driver.execute_script("window.open(arguments[0]);", url)
        print("All URLs opened in tabs.")
        last_check_time = time.time()

        def trigger_manual_check():
            print("Manual check triggered with F5.")
            check_all_tabs(driver, open_urls)
            save_urls_to_file(session_file, open_urls)
            print("URLs saved to file.")

        def on_press(key):
            try:
                if key == keyboard.Key.f5:
                    trigger_manual_check()
            except AttributeError:
                pass

        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        while True:
            time.sleep(1)
            current_handles = driver.window_handles
            if len(current_handles) == 0:
                print("Browser closed")
                break
            current_url = driver.current_url
            if current_url not in open_urls:
                print(f"New URL detected: {current_url}")
                open_urls.add(current_url)
            if time.time() - last_check_time >= 300:
                check_all_tabs(driver, open_urls)
                last_check_time = time.time()
    except FileNotFoundError:
        print(f"Error: The '{name}' file does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    finally:
        save_urls_to_file(session_file, open_urls)
        if driver:
            driver.quit()


def check_all_tabs(driver, open_urls):
    print("Checking all open tabs...")
    current_handles = driver.window_handles
    for handle in current_handles:
        try:
            driver.switch_to.window(handle)
            current_url = driver.current_url
            if current_url not in open_urls:
                print(f"New URL detected in tab: {current_url}")
                open_urls.add(current_url)
        except NoSuchWindowException:
            print("Warning: Tried to access a closed window/tab.")
    print("URLs updated")


def save_urls_to_file(file_path, urls):
    try:
        with open(file_path, "w") as f:
            for url in urls:
                f.write(f"{url}\n")
    except IOError as e:
        print(f"Error saving URLs to file: {str(e)}")

