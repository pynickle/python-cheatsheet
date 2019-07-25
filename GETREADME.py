import requests


def main():
    url = "https://raw.githubusercontent.com/pynickle/python-cheatsheet/master/README.md"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3858.0 Safari/537.36"}

    r = requests.get(url, headers=headers)
    f = open("python-cheatsheet.md", "w", encoding="utf-8")

    res = r.text.replace("\r\n", "\n")
    print(res, file = f)

    f.close()

if __name__ == "__main__":
    main()
