import textnode
import os
import shutil
from pathlib import Path
from block_markdown import markdown_to_html_node 
from htmlnode import HTMLNode
from extract_title import extract_title

def main():
    pass

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def copy_contents(source_dir, target_dir, is_initial_call=True):
    if is_initial_call:
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)
            print('target directory removed')

        os.mkdir(target_dir)
        print('public directory created')

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        target_path = os.path.join(target_dir, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, target_dir)
            print(f'copying {item} to {target_dir}')

        if os.path.isdir(source_path):
            if not os.path.exists(target_path):
                os.mkdir(target_path)
                print(f'Directory {target_path} created.')
            copy_contents(source_path, target_path, False)

def generate_page(from_path, template_path, dest_path):
    #print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as my_file:
        markdown= my_file.read()
    with open(template_path) as my_file:
        template_path_variable = my_file.read()
    md_to_node = markdown_to_html_node(markdown)
    node_to_html = md_to_node.to_html()
    title = extract_title(markdown)
    html_title = template_path_variable.replace('{{ Title }}', title)
    full_content = html_title.replace('{{ Content }}', node_to_html)
    destination_dir = os.path.dirname(dest_path)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(full_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


main()
#copy_contents(source_dir, target_dir)
print("Generating content...")
generate_pages_recursive(dir_path_content, template_path, dir_path_public)