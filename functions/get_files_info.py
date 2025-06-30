import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        target_directory = os.path.abspath(working_directory)
        if directory:
            target_directory = os.path.abspath(os.path.join(working_directory, directory))
        if not target_directory.startswith(os.path.abspath(working_directory)):
            return 'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'
        contents = os.listdir(target_directory)
        content_strings = []
        for content in contents:
            name = content
            filepath = os.path.join(target_directory, name)
            file_size = os.path.getsize(filepath)
            is_dir = os.path.isdir(filepath)
            content_strings.append(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(content_strings)
    except Exception as e:
        return f"Error encountered: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
