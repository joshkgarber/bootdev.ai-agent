import os

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

