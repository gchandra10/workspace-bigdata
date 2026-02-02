import platform
import subprocess
import sys

print(f"Operating System: {platform.system()} {platform.release()}")

print(f"Python Version: {sys.version}")


def check_tool(name):
    try:
        subprocess.run([name, "--version"], capture_output=True)
        print(f"YES! {name} is installed.")
    except FileNotFoundError:
        print(f"NO! {name} is MISSING.")


check_tool("az")
check_tool("terraform")
check_tool("ruff")
check_tool("uv")
