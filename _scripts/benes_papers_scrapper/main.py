import os
from os.path import exists, join
import sys
from urllib import request, parse, error
# The BIBTEX library
import biblib.bib

# Import common functions for handling papers
sys.path.append('..')
from bib_utils.bib_utils import format_pdf_filename, format_image_filename

# Reference BIB file 
bib_file = 'benes_original_references.bib'
images_folder = '../../resources/images/supplemental'
papers_folder = '../../resources/papers'
url_images = 'http://hpcg.purdue.edu/bbenes/images/pubPic/'
url_papers = 'http://hpcg.purdue.edu/bbenes/papers/'


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
