"""File management"""
import os
import json


def create(file_name: str, content: list | dict = None) -> None:
    """Create a new json file

    Args:
        file_name (str): File name or path
        content (str, optional): Text file content. Defaults to None.
    """
    mode = "w" if content else "x"

    try:
        file = open(file_name, mode)

    except FileExistsError as error:
        raise OSError(f"File '{file_name}' already exists") from error

    except PermissionError as error:
        raise OSError(f"You do not have permisson to create '{file_name}'") from error

    if content and isinstance(content, (list, dict)):
        content = json.dumps(content)
        file.write(content)

    file.close()


def update(file_name: str, content: list | dict) -> None:
    """Updates an existing file

    Args:
        file_name (str): File name or path
        content (str): Text file content
        overwrite (bool, optional): If True, file will be overwritten. Defaults to False.
    """
    if not isinstance(content, dict | list) or content == "":
        raise ValueError("'content' argument must be specified")

    file = open(file_name)
    file_content = json.loads(file.read())
    file.close()

    if isinstance(file_content, list):
        if isinstance(content, dict):
            file_content.append(content)

        elif isinstance(content, list):
            file_content += content

    elif isinstance(file_content, dict):
        if isinstance(content, dict):
            file_content = [file_content, content]

        elif isinstance(content, list):
            file_content = [file_content] + content

    file = open(file_name, "w")
    file.write(json.dumps(file_content))
    file.close()


def read(file_name: str) -> str:
    """Returns the content of a existing file

    Args:
        file_name (str): File name or path

    Returns(str): File content
    """
    try:
        file = open(file_name)

    except FileNotFoundError as error:
        raise OSError(f"File '{file_name}' not exists") from error
    
    content = json.loads(file.read())
    file.close()
    return content