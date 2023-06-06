import subprocess

def run_os_command(command):
    """
    Run a command on the operating system and return the output.
    """
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        output = str(output.strip(), 'utf-8')
    except subprocess.CalledProcessError as e:
        output = str(e.output.strip(), 'utf-8')
    return output
