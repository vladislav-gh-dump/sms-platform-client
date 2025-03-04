import platform
import subprocess
import os


DIR_PATH = f"{os.getcwd()}/mock_server/"

prism_cli_collection = {
    "Linux": "prism-cli-linux",
    "Darwin": "prism-cli-macos",
    "Windows": "prism-cli-win.exe",   
}


def main():
    os_name = platform.system()
    prism_cli = prism_cli_collection[os_name]
    command = f"{DIR_PATH}{prism_cli} mock {DIR_PATH}sms-platform.yaml"
    subprocess.run(command, shell=True)
    

if __name__ == "__main__":
    main()
