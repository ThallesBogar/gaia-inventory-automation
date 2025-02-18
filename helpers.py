import os

import streamlit as st

# @st.cache_resource()
def load_css(css_file: str) -> str:
    primary_color = st.get_option('theme.primaryColor')

    with open(css_file, 'r') as f:
        css_content = ' '.join(f.read().split())
        css_content = css_content.replace('%primary_color%', f'{primary_color}')

        return f'<style>{css_content}</style>'


def load_svg_icon(icon_name: str) -> str:
    file_name = f'{icon_name}.svg'
    current_path = os.path.dirname(__file__)
    icons_path = os.path.join(current_path, 'assets/icons')
    svg_file_path = os.path.join(icons_path, file_name)
    primary_color = st.get_option('theme.primaryColor')

    with open(svg_file_path, 'r') as f:
        svg_content = ' '.join(f.read().split())
        svg_content = svg_content.replace('%primary_color%', f'{primary_color}')

        return svg_content


def load_template(template_name: str) -> str:
    file_name = f'{template_name}.html'
    current_path = os.path.dirname(__file__)
    templates_path = os.path.join(current_path, 'views/templates')
    html_file_path = os.path.join(templates_path, file_name)

    with open(html_file_path, 'r') as f:
        html_content = ' '.join(f.read().split())

        return html_content


def get_input_label(label: str, icon: str) -> str:
    icon = load_svg_icon(icon)
    html = load_template('input_label')

    html = html.replace('{label}', label)
    html = html.replace('{icon}', icon)

    return html
