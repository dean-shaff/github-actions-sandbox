
def main():
    with open("README.template.md", "r") as fd:
        contents = fd.read()

    contents = contents.format(help="Hello from Github Actions Sandbox!")

    with open("README.md", "w") as fd:
        fd.write(contents)


if __name__ == "__main__":
    main()
