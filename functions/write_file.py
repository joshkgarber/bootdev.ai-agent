import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        abs_wdf = os.path.abspath(os.path.join(working_directory, file_path))
        if not abs_wdf.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory.'
        if not os.path.exists(os.path.dirname(abs_wdf)):
            os.makedirs(os.path.dirname(abs_wdf))
        with open(abs_wdf, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error encountered: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to the specified file if it exists in the working directory. Overwrites the file contents if it already exists.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to (relative to the working directory).",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file.",
            ),
        },
    )
)
