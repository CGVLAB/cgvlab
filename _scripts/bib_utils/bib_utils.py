"""
Collection of functions useful for manipulating bibtex entries
"""

import os

def format_string(string):
    # Replace special characters
    string = string.replace('{\\\'\\i}', 'i')
    string = string.replace('{\\v{c}}', 'c')
    string = string.replace('{\\\'a}', 'a')
    string = string.replace('{\\\'{a}}', 'a')
    string = string.replace('{\\v{S}}', 'S')
    string = string.replace('{\\v{s}}', 's')
    string = string.replace('{\\v{Z}}', 'Z')
    string = string.replace('{\\v{r}}', 'r')
    string = string.replace('{\\\'e}', 'e')
    string = string.replace('{\\"a}', 'a')
    string = string.replace('{\\v{t}}', 't')

    # Remove dots
    string = string.replace('.', '')
    # Remove '
    string = string.replace('\'', '')
    string = string.replace('’', '')
    # Remove /
    string = string.replace('/', '')
    # Remove \
    string = string.replace('\\', '')
    # Remove &
    string = string.replace('&', '')
    # Remove {}
    string = string.replace('{', '')
    string = string.replace('}', '')
    # Remove :
    string = string.replace(':', '')
    # Remove ;
    string = string.replace(';', '')
    # Underscore are doubled
    string = string.replace('_', '__')
    # Double hyphens are removed
    string = string.replace('--', '-')
    # Spaces become underscores
    string = string.replace(' ', '_')

    return string


def find_first_author_name(authors):
    # Get everything before the first space or the first comma
    index_space = authors.find(' ')
    index_comma = authors.find(',')

    # Extract last char of the author name
    substr_end = len(authors) - 1
    if index_space >= 0:
        substr_end = min(substr_end, index_space)
    if index_comma >= 0:
        substr_end = min(substr_end, index_comma)

    return authors[0:substr_end]


def truncate(string):
    if len(string) > 64:
        return string[0:64]
    else:
        return string


def format_pdf_filename(entries):
    filename_entries = []

    if 'author' in entries:
        filename_entries.append(format_string(find_first_author_name(entries['author'])))

    if 'journal' in entries:
        filename_entries.append(truncate(format_string(entries['journal'])))

    if 'year' in entries:
        filename_entries.append(format_string(entries['year']))

    if 'title' in entries:
        filename_entries.append(truncate(format_string(entries['title'])))

    return '-'.join(filename_entries) + '.pdf'


def format_image_filename(entries):
    filename_entries = []
    extension = ''

    if 'author' in entries:
        filename_entries.append(format_string(find_first_author_name(entries['author'])))

    if 'year' in entries:
        filename_entries.append(format_string(entries['year']))

    if 'title' in entries:
        filename_entries.append(truncate(format_string(entries['title'])))

    filename_entries.append('thumbnail')

    if 'image' in entries:
        split_filename = os.path.splitext(entries['image'])
        extension = split_filename[1]

    return '-'.join(filename_entries) + extension.lower()
