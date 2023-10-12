import platform
import subprocess
import datetime

# def list_files(startpath):
#     fs = subprocess.check_output([['tree', '-I venv'], startpath]).decode().split('\n')
#     return str(fs)

def get_system_info():
    # Get basic system info
    os = platform.system()
    distribution = platform.release()
    version = platform.version()
    user = subprocess.check_output(['whoami']).decode().strip()
    memory = subprocess.check_output(['free', '-m']).decode().split()[7]
    pip_list = subprocess.check_output(['pip', 'list']).decode().strip()
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    command = "apt list --installed"

    result = subprocess.run(command, shell=True, capture_output=True)
    output = result.stdout.decode()

    apt_installed = []
    for line in output.splitlines():
        app = line.split()[0]
        apt_installed.append(app)

    # Prepare output
    output = {
        'DATE_TIME': date_time + '\n',
        'DIGITAL_HAMLET_PATH': '/home/cplan/dev/The-Digital-Hamlet\n',
        'ARCHITECT_PATH': '/home/cplan/dev/The-Digital-Hamlet/src/architect\n',
        'OS': os + '\n',
        'Kernel': distribution + '\n',
        'Distribution': version + '\n',
        'User': user + '\n',
        'Memory': f'{memory}GB\n',
        'Pip installed': pip_list + '\n',
        'APT installed': apt_installed + '\n'
    }
    output_string = ''
    for key, value in output.items():
        output_string += f'{key}: {value}'
    return output_string