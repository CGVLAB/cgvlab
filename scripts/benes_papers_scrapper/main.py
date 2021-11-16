import os
from os.path import exists, join
import sys
from urllib import request, parse, error

# Load the BIBTEX library
sys.path.append('biblib')
import biblib.bib

# Reference BIB file 
bib_file = 'benes_original_references.bib'
images_folder = '../../resources/images/supplemental'
papers_folder = '../../resources/papers'
url_images = 'http://hpcg.purdue.edu/bbenes/images/pubPic/'
url_papers = 'http://hpcg.purdue.edu/bbenes/papers/'

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


def main():
    with open(bib_file, 'r') as fp:
        db = biblib.bib.Parser().parse(fp, log_fp=sys.stderr).get_entries()

        for entries in db.values():
            key = entries.key

            if 'image' in entries:
                image_file = entries['image']
                new_image_filename = format_image_filename(entries)
                new_image_path = join(images_folder, new_image_filename)

                # Check that the file is not already present in the folder
                if not exists(new_image_path):
                    # Download the file from internet
                    url_image = parse.urljoin(url_images, image_file)
                    try:
                        request.urlretrieve(url_image, new_image_path)
                    except error.HTTPError:
                        print('Failed to download image for {}'.format(key), file=sys.stderr)
                
                # Replace the name in the bib file
                entries['image'] = new_image_filename

            if 'pdf' in entries:
                pdf_file = entries['pdf']
                new_pdf_filename = format_pdf_filename(entries)
                new_pdf_path = join(papers_folder, new_pdf_filename)
                
                # Check that the file is not already present in the folder
                if not exists(new_pdf_path):
                    # Download the file from internet
                    url_paper = parse.urljoin(url_papers, pdf_file)
                    try:
                        request.urlretrieve(url_paper, new_pdf_path)
                    except error.HTTPError:
                        print('Failed to download PDF for {}'.format(key), file=sys.stderr)
                
                # Replace the name in the bib file
                entries['pdf'] = new_pdf_filename

            print(entries.to_bib(wrap_width=250))


if __name__ == "__main__":
    main()
