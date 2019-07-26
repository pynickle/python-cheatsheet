import doctest


def main(file_name):
    status = None
    code = ""
    with open(file_name, "r", encoding="utf-8") as f:
        r = f.readlines()
        for i in r:
            if not status:
                if i.strip().startswith("```"):
                    status = 1
                    continue
            else:
                if i.strip().startswith("```"):
                    status = None
                    continue
                else:
                    code += i
    return code

if __name__ == "__main__":
    code = main("README.md")
    # print(code)
    doctest.run_docstring_examples(code, None)