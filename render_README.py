import sys


def render(input_file_path, output_file_path, content):

    with open(input_file_path, "r") as fd:
        new_content = fd.read()

    new_content = new_content.format(help=content)

    with open(output_file_path, "w") as fd:
        fd.write(new_content)


def main():
    content = sys.stdin.read()
    render("README.template.md", "README.md", content)


if __name__ == "__main__":
    main()
