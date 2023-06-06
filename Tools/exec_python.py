def run_exec_python(code: str):
    """
    Execute Python code and return the output.
    """
    try:
        output = str(eval(code))
    except Exception as e:
        output = str(e)
    return output
