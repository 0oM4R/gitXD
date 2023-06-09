# Step 1,2
```python
import argparse

def main():
    args = parse_args()
    args.func (args)

def parse_args():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command")
    commands.required = True

    init_parser = commands.add_parser("init")
    init_parser.set_defaults (func=init)
    
    return parser.parse_args ()

def init (args):
    print("hello world")
```

## Explanation
The code begins by importing the argparse module, which provides a convenient way to parse command-line arguments.

The main() function serves as the entry point for the program. It is responsible for parsing the command-line arguments and executing the appropriate function based on the command provided.

Inside the main() function, parse_args() is called to parse the command-line arguments and return an args object.

The parse_args() function is where the command-line arguments are defined and parsed. It creates an argparse.ArgumentParser object, which is used to define and parse the command-line arguments.

The commands variable is assigned to the add_subparsers() method of the parser object. This creates a container for the sub-commands that can be executed.

commands.required = True is set to ensure that a sub-command is provided when running the script. Without a sub-command, an error will be raised.

init_parser is defined as a sub-parser for the "init" command. This creates a specific command that can be executed when "init" is provided as a sub-command.

init_parser.set_defaults(func=init) sets the default function to be executed when the "init" command is given. In this case, the init() function will be called.

Finally, the parse_args() function returns the parsed command-line arguments.

Back to main function, The line args.func(args) is responsible for executing the appropriate function based on the command provided by the user.
The init() function is defined to handle the "init" command. In this case, it simply prints the message "hello world".gi

## Step 3

__Adding .xD directory__
Git stores all repository data locally, in a subdirectory called ".git", so upon initialization we'll create one; using os, will name it `.xD`

## Step 4

create object database

- It allows us to store and retrieve arbitrary blobs, which are called "objects".
- So the flow of the command hash-object is:
  - Get the path of the file to store.
  - Read the file.
  - Hash the content of the file using SHA-1.
  - Store the file under ".ugit/objects/{the SHA-1 hash}".

This type of storage is called content-addressable storage because the "address" that we use to find a blob is based on the content of the blob itself.
When real Git stores objects it does a few extra things, such as writing the size of the object to the file as well, compressing them and dividing the objects into 256 directories. This is done to avoid having directories with huge number of files, which can hurt performance. We're not going to do this in ugit for simplicity.
