import os

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

