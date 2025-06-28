import os

MAX_CHARS = 10000

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

