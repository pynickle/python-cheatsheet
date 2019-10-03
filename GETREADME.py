from sys import exit
import time

import requests


def main(choice):
    start = time.time()
    if choice == "1":
        url = "https://raw.githubusercontent.com/pynickle/python-cheatsheet/master/README-zh-cn.md"
    else:
        url = "https://raw.githubusercontent.com/pynickle/python-cheatsheet/master/README.md"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3858.0 Safari/537.36"}

    print("Requesting...")
    r = requests.get(url, headers=headers)
    f = open("python-cheatsheet.md", "w", encoding="utf-8")

    print("Processing...")
    res = r.text.replace("\r\n", "\n")
    print(res, file=f)

    print("Saving...")
    f.close()

    print(f"Using: {time.time()-start:.2f} s")


if __name__ == "__main__":
    choice_range = ["1", "2"]
    choice = input("Chinese(1) or English(2): ")
    if choice not in choice_range:
        print("Invalid Choice!")
        exit()
    main(choice)
