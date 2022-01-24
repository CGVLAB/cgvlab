import os
from os import listdir
from os.path import exists, join, isfile
import sys
from urllib import request, parse, error
# Package for fuzzy matching
from fuzzywuzzy import fuzz
# The BIBTEX library
import biblib.bib

# Import common functions for handling papers
sys.path.append('..')
from bib_utils.bib_utils import format_pdf_filename, format_image_filename

# Reference BIB file 
bib_file = '../../_bibliography/references.bib'
images_folder = '../../resources/images/supplemental'
papers_folder = '../../resources/papers'

# Threshold for duplicates
#  - close to 0 => everything is duplicate
#  - close to 100 => only exact same titles are duplicates
duplicate_threshold = 80

# Whether to display warnings/errors or not
errors_activated = True
warning_activated = False
info_activated = False


def log_err(message):
    if errors_activated:
        print('Error: ', message)


def log_warn(message):
    if warning_activated:
        print('Warning: ', message)


def log_info(message):
    if info_activated:
        print('Info: ', message)


def list_files(folder):
    """ List all files in a directory """
    list_files = []

    for file in listdir(folder):
        file_path = join(folder, file)
        if isfile(file_path):
            list_files.append(file)

    return list_files


def list_entries(entry_name):
    """ List values referenced by a certain entry (for example: pdf, image) """
    list_entries = []

    with open(bib_file, 'r') as fp:
        db = biblib.bib.Parser().parse(fp, log_fp=sys.stderr).get_entries()

        for entries in db.values():
            key = entries.key

            if entry_name in entries:
                list_entries.append(entries[entry_name])

    return list_entries


def list_entries_without_property(entry_name):
    """ List entries without a certain property (for example: papers without images) """
    list_entries = []

    with open(bib_file, 'r') as fp:
        db = biblib.bib.Parser().parse(fp, log_fp=sys.stderr).get_entries()

        for entries in db.values():
            key = entries.key

            if entry_name not in entries:
                list_entries.append(entries)

    return list_entries


def check_paper_database():
    with open(bib_file, 'r') as fp:
        db = biblib.bib.Parser().parse(fp, log_fp=sys.stderr).get_entries()

        for entries in db.values():
            key = entries.key

            # Check that the image exists
            if 'image' in entries:
                image_file = entries['image']
                image_path = join(images_folder, image_file)

                # Check that the file is not present in the folder
                if not exists(image_path):
                    # Display error
                    log_err('paper {} image does not exist'.format(key))
            else:
                # Display a warning because this paper has no image
                log_warn('paper {} has no image associated'.format(key))

            # Check that the PDF exists
            if 'pdf' in entries:
                pdf_file = entries['pdf']
                pdf_path = join(papers_folder, pdf_file)

                # Check that the file is not present in the folder
                if not exists(pdf_path):
                    # Display error
                    log_err('paper {} PDF does not exist'.format(key))
            else:
                # Display a warning because this paper has no image
                log_warn('paper {} has no PDF associated'.format(key))


def check_image_correspondence():
    # List of image files that are allowed to be in the image folder
    allowed_files = list_entries('image')

    # Add default files
    allowed_files.append('default.png')
    allowed_files.append('default.jpg')

    for file in listdir(images_folder):
        file_path = join(images_folder, file)
        if isfile(file_path):
            # Check that the file is in the list of allowed files
            if file not in allowed_files:
                # Print an error if the file is not referenced in any publication
                log_err('image {} is not referenced by any paper'.format(file))


def check_pdf_correspondence():
    # List of PDF files that are allowed to be in the PDF folder
    allowed_files = list_entries('pdf')

    # Add gitignore
    allowed_files.append('.gitignore')

    for file in listdir(papers_folder):
        file_path = join(papers_folder, file)
        if isfile(file_path):
            # Check that the file is in the list of allowed files
            if file not in allowed_files:
                # Print an error if the file is not referenced in any publication
                log_err('PDF {} is not referenced by any paper'.format(file))


def check_for_duplicates():
    # List of all titles
    all_titles = list_entries('title')

    for i in range(len(all_titles)):
        for j in range(i + 1, len(all_titles)):
            ratio = fuzz.ratio(all_titles[i].lower(), all_titles[j].lower())
            if ratio > duplicate_threshold:
                log_err('Possible duplicates:\n\t{}\n\t{}'.format(all_titles[i], all_titles[j]))


def make_image_recommendation():
    """ For entries without image, make a recommendation for an image """
    files = list_files(images_folder)
    entries_without_image = list_entries_without_property('image')

    for entry in entries_without_image:
        
        # Remove spaces in title
        title_no_space = entry['title'].replace(' ', '')

        # Match with files in the list
        best_match_ratio = 0
        best_match_index = 0
        for i in range(len(files)):
            ratio = fuzz.ratio(title_no_space.lower(), files[i].lower())
            if ratio > best_match_ratio:
                best_match_ratio = ratio
                best_match_index = i

        if best_match_ratio > duplicate_threshold:
            log_info('Recommended image for paper:\n\t{}\n\t{}'.format(entry['title'], files[best_match_index]))


def main():
    check_paper_database()
    check_image_correspondence()
    check_pdf_correspondence()
    check_for_duplicates()
    # make_image_recommendation()

    # TODO: list all papers without PDF
    # TODO: list all papers without image


if __name__ == "__main__":
    main()
