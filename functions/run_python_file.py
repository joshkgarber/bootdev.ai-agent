import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    wdf = os.path.join(working_directory, file_path)
    abs_wdf = os.path.abspath(wdf)
    abs_wd = os.path.abspath(working_directory)
    if not abs_wdf.startswith(abs_wd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_wdf):
        return f'Error: File "{file_path}" not found.'
    if not file_path.split(".")[-1] == "py":
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python3", abs_wdf]
        if args:
            commands.extend(args)
        output = subprocess.run(
            commands,
            timeout=30,
            capture_output=True,
            text=True,
            cwd=abs_wd,
        )
        result = []
        if output.stdout:
            result.append(f"STDOUT:\n{output.stdout}")
        if output.stderr:
            result.append(f"STDERR\n{output.stderr}")
        return_code = output.returncode
        if return_code != 0:
            result += f" Process exited with code {return_code}"
        if not result:
            result = "No output produced."
        return result
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="executes a Python file within the working directory returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"]
    ),
)

