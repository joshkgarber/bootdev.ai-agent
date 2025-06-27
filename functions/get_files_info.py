import os

MAX_CHARS = 10000

def get_files_info(working_directory, directory=None):
    try:
        abs_wdd = os.path.abspath(os.path.join(working_directory, directory))
        if not abs_wdd.startswith(os.path.abspath(working_directory)):
            return 'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(abs_wdd):
            return f'Error: "{directory}" is not a directory'
        contents = os.listdir(abs_wdd)
        content_strings = []
        for content in contents:
            name = content
            filepath = os.path.join(abs_wdd, name)
            file_size = os.path.getsize(filepath)
            is_dir = os.path.isdir(filepath)
            content_strings.append(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(content_strings)
    except Exception as e:
        return f"Error encountered: {e}"


def get_file_content(working_directory, file_path):
    try:
        abs_wdf = os.path.abspath(os.path.join(working_directory, file_path))
        if not abs_wdf.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_wdf):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(abs_wdf, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) == 10000:
            file_content_string += f'[... File "{file_path}" truncated at 10000 characters]'
        return file_content_string
    except Exception as e:
        return f"Error encountered: {e}"

