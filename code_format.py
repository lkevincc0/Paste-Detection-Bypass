def code_format(code):
    lines = code.split('\n')
    formatted_lines = [f'"{line}"' if line.strip() else '""' for line in lines]
    return formatted_lines