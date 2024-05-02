import re

def extract_markdown_images(text):
    return list(map(tuple, re.findall(r"!\[(.*?)\]\((.*?)\)", text)))
    
def extract_markdown_links(text):
    print(list(map(tuple, re.findall(r"\[(.*?)\]\((.*?)\)", text))))



extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)")
text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
extract_markdown_links(text)