import doctest
import re


NOTEST = ["random.random", "random.randint", "random.randrange",
          "random.uniform", "codecs.getdecoder", "codecs.getencoder",
          "time.ctime", "time.perf_counter", "time.strftime",
          "time.localtime", "os.getcwd", "os.name", "secrets.choice"]


def main(file_name):
    status = None
    code = ""
    with open(file_name, "r", encoding="utf-8") as f:
        r = f.readlines()
        for i in r:
            if not status:
                if i.strip().startswith("```"):
                    status = "code"
                    continue
            elif status == "notest":
                if i.startswith(">>>"):
                    status = "code"
                else:
                    continue
            if status == "code":
                for item in NOTEST:
                    if re.search(item, i):
                        status = "notest"
                        break
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
