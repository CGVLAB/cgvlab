# CGVLab Website

This is the website of our academic research group - the [Computer Graphics and Visualization Laboratory](http://wiki.cs.purdue.edu/cgvlab/doku.php) at [Purdue University](https://purdue.edu).

This website is powered by Jekyll and Bootstrap (with Bootswatch). It is forked from the [Allan Lab at Leiden University](https://www.allanlab.org/) website.

# Updating

The conventions and process for adding papers and related material are outlined below.

## Conventions

### Papers

All papers are expected to be in PDF (.pdf) format and named with the following standard:

`<PRIMARY AUTHOR>-<JOURNAL NAME>-<YEAR>-<PAPER TITLE>.pdf`

**Rules**

1. Replace <Text\> with its value (e.g. "<PRIMARY AUTHOR\>" becomes "Smith")
2. All spaces must be replaced with underscores (e.g. "A Paper on Stuff" becomes "A_Paper_on_Stuff")
3. Should any fields contain hyphens or underscores, double them (e.g. "Generic-Journal_Name" becomes "Generic--Journal__Name")
4. The file extension should be lowercase (e.g. ".PDF" is not allowed, use ".pdf")

**Example**

`Anderson-The_Visual_Computer-2016-VR_Annotations_of_the_Surgical_Field_through_an_AR_Transparent_Display.pdf`

### Files

All additional files (images, videos, etc.) should be named with the following standard:

`<PRIMARY AUTHOR>-<YEAR>-<PAPER TITLE FIRST WORD(S)>-<IMAGE TITLE>.<FILE EXTENSION>`

**Rules**

1. Replace <Text\> with its value (e.g. "<PRIMARY AUTHOR\>" becomes "Smith")
2. All spaces must be replaced with underscores (e.g. "A Paper on Stuff" becomes "A_Paper_on_Stuff")
3. Should any fields contain hyphens or underscores, double them (e.g. "Generic-Journal_Name" becomes "Generic--Journal__Name")
4. The file extension should be lowercase (e.g. ".JPG" is not allowed, use ".jpg")

**Example**

(Not an actual file)

`Anderson-2016-VR_Annotations-Annotation_Example.jpg`

### BibTeX

The format for a BibTeX entry should generally be like the following standard:

```
@<ENTRY TYPE, USUALLY "inproceedings" OR "article">{<AUTHOR LAST NAME><YEAR><FIRST WORD(S) OF TITLE>,

    ...

  highlighted  = {<SET TO "true" IF THIS PAPER SHOULD BE HIGHLIGHTED, "false" IF NOT>},
  doi          = {<DOI ONLY>},
  pdf          = {<PDF FILE NAME IN THE UPLOAD DIRECTORY>}
  image        = {<FILE NAME(S) (SPACE-SEPARATED) OF IMAGES>}
  video        = {<FILE NAME(S) (SPACE-SEPARATED) OF VIDEOS>}
  link         = {<LINK(S) (SPACE-SEPARATED) TO EXTERNAL WEBSITE>}
}
```

**Rules**

Replace `...` with the other standard BibTeX values (author(s), title, etc.).

**Example**

```
@article{andersen2016virtual,
  title     = {Virtual annotations of the surgical field through an augmented reality transparent display},
  author    = {Andersen, Daniel and Popescu, Voicu and Cabrera, Maria Eugenia and Shanghavi, Aditya and Gomez, Gerardo and Marley, Sherri and Mullis, Brian and Wachs, Juan},
  journal   = {The Visual Computer},
  volume    = {32},
  number    = {11},
  pages     = {1481--1498},
  year      = {2016},
  publisher = {Springer},
  doi       = {10.1007/s00371-015-1135-6},
  pdf       = {Anderson-The_Visual_Computer-2016-VR_Annotations_of_the_Surgical_Field_through_an_AR_Transparent_Display.pdf}
}
```

## Process

To add a paper to the repository, follow these steps:

1. Ensure your paper is PDF named with the conventions above, you have your supplemental files (images, videos, etc.) named with the conventions above, and a BibTeX entry like above
2. Open the file [bibliography/references.bib](./bibliography/references.bib) and append your BibTeX entry beneath the last entry
3. Copy your PDF file into the [resources/papers](./resources/papers) directory
4. Copy your image(s) into the [resources/images/supplemental](./resources/images/supplemental) directory, video(s) to [resources/videos/supplemental](./resources/videos/supplemental), and other file(s) to [resources/files/supplemental](./resources/files/supplemental)
5. Finally, add the files, commit, and push to the remote repository

# Building

To build for production, run `JEKYLL_ENV="production" bundle exec jekyll build`.

# Copyright

CGVLab Website. Copyright (c) 2020 CGVLab. Code released under the [MIT License](./LICENSE).
