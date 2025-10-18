"""
    This program takes in a name of a file with its extension and returns
    the file type of the file.
"""


def main():
    # Get input for file name:
    file_name: str = get_str_input_lower("File_name: ")

    # Determine whether the answer is correct:
    print(file_type_check(file_name))


# Get str input in lower case
def get_str_input_lower(prompt: str) -> str:
    return (input(prompt).lower())


def file_type_check(name: str) -> str:
    # Determine what the name ends with:
    if "." in name:
        extension = name.rsplit('.')
        match extension[1]:
            case "gif":
                return "image/gif"
            case "jpg":
                return "image/jpeg"
            case "jpeg":
                return "image/jpeg"
            case "png":
                return "image/png"
            case "pdf":
                return "application/pdf"
            case "txt":
                return "text/plain"
            case "zip":
                return "application/zip"
            case _:
                return "application/octet-stream"
    else:
        return "application/octet-stream"


if __name__ == "__main__":
    main()
