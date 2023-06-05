import subprocess

def run_custom_command(command):
    """
    Run a custom command on the operating system.
    """
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        output = str(output.strip(), 'utf-8')
    except subprocess.CalledProcessError as e:
        output = str(e.output.strip(), 'utf-8')
    return output
