def extract_title(markdown):
    lines = markdown.split("\n")
    heading_1 = None
    for line in lines:
        if line.startswith("# "):
            heading_1 = line
            break
    if heading_1 == None:
        raise Exception('Text needs heading 1')
    return heading_1[2:]