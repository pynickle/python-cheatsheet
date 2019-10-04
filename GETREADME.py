from sys import exit
import time
import re
import codecs

import requests


def get_all_code(file_name):
    status = None
    all_code = []
    code = ""
    with codecs.open(file_name, "r", encoding="utf-8") as f:
        r = f.readlines()
        all_data = "".join(r)
        for i in r:
            if not status:
                if i.strip().startswith("```"):
                    status = "code"
                    continue
            if status == "code":
                if i.strip().startswith("```"):
                    status = None
                    all_code.append(code)
                    code = ''
                    continue
                else:
                    code += i
    return all_code, all_data

def without_prefix(all_code):
    all_code_without_prefix = []
    for code in all_code:
        lst = code.split("\n")
        result = ""
        for i in lst:
            if i.startswith(">>> "):
                i = i.replace(">>> ", "") + "\n"
            elif i.startswith("... "):
                i = i.replace("... ", "") + "\n"
            elif i == "..." or i == ">>>":
                i = "" + "\n"
            else:
                i = ""
            result += i
        all_code_without_prefix.append(result)
    return all_code_without_prefix

def replace(all_data, all_code_without_prefix):
    for i in all_code_without_prefix:
        all_data = re.sub(r"```((.*?)\n)>>> ((.*?)\n)*?```", "```\n" + i.replace(r"\W", "\\\\W").replace(r"\x", "\\\\x") + "```\n", all_data, 1)
    return all_data

def main(choice1, choice2):
    start = time.time()
    if choice1 == "1":
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

    if choice2 == "2":
        print("Removing...")
        all_code, all_data = get_all_code("python-cheatsheet.md")
        all_code_without_prefix = without_prefix(all_code)
        all_data = replace(all_data, all_code_without_prefix)
    with open("python-cheatsheet.md", "w", encoding="utf-8") as f:
        f.write(all_data)

    print(f"Using: {time.time()-start:.2f} s")


if __name__ == "__main__":
    choice_range = ["1", "2"]
    choice1 = input("Chinese(1) or English(2): ")
    if choice1 not in choice_range:
        print("Invalid Choice!")
        exit()
    
    choice2 = input("With command line code prefix(1) or not(2): ")
    if choice2 not in choice_range:
        print("Invalid Choice!")
        exit()

    main(choice1, choice2)
