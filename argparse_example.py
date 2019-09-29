import argparse

parser = argparse.ArgumentParser(description="the example parser for argparse")

parser.add_argument("-a", type=int, help="the a number for adding")
parser.add_argument("-b", type=int, help="the b number for adding")

parser.add_argument("-s", "--sum", nargs="+", type=int)
parser.add_argument("-r", "--required", required=True)
parser.add_argument("-t", "--true", action="store_true")

args = parser.parse_args()
print(args)

print(args.a + args.b)

res = 0
for i in args.sum:
    res += i
print(res)