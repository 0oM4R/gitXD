import argparse
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate factorial of 5

def main():
    args = parse_args()
    args.func (args)

def parse_args():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="init")
    commands.required = True

    init_parser = commands.add_parser("init")
    init_parser.set_defaults (func=init)
    
    return parser.parse_args ()

def init (args):
    print("Hello, world!")
