# Generates a page for each publication
# Pages are located at /publications/<key>/index.html
# Uses the BibTeX file _bibliography/references.bib
# Jekyll-Scholar provides functionality to do this, but our custom plugin has more more capabilities 
# Each page can have customized content by creating a .html file with the publications's key in _include/_publication

require 'bibtex'
require 'citeproc'
require 'csl/styles'

module Jekyll
  class PublicationPageGenerator < Generator
    safe true

    def generate(site)
      # Check if this layout exists

      layout = 'publication'
      dir = 'publications'

      if site.layouts.key? layout

        # Load and format bibliography with MLA
        bib = BibTeX.open('_bibliography/references.bib')
        cp = CiteProc::Processor.new style: 'modern-language-association', format: 'text'
        cp.import bib.to_citeproc

        # Create page for each publication
        for publication in bib
          # Render citation
          citation = cp.render :bibliography, id: publication.id
          # Save page
          site.pages << PublicationPage.new(site, site.source, File.join(dir, publication.key), publication, citation)
        end
      end
    end
  end

  # A Page subclass used in the `PublicationPageGenerator`
  class PublicationPage < Page
    def initialize(site, base, dir, publication, citation)
      # Initialize internal variables
      @site = site
      @base = base
      @dir = dir
      @citation = citation
      @name = 'index.html'

      # Initialize other variables
      @fname = publication.key + '.html'
      @publication = publication
      @customize_dir = File.join(base, '_pages', '_publication', @fname);
      @publication_dir = File.join(base, '_layouts', 'publication.html')
      
      # Create file and load layout file
      self.process(@name)
      self.read_yaml(File.dirname(@publication_dir), File.basename(@publication_dir))

      # Set page properties
      # Accessible in Liquid via `page.<property>` (e.g. `page.title`)

      self.data['publication_title'] = @publication['title']
      self.data['publication_year'] = @publication['year']
      self.data['publication_source'] = @publication['booktitle'] || @publication['journal'] || @publication['publisher'] || 'Unknown'

      # Retrieve all authors

      @faculty = site.data['faculty'].map{|s| s.merge!('type' => 'faculty') }
      @students = site.data['students'].map{|s| s.merge!('type' => 'student') }
      @former_members = site.data['former_members'].map{|s| s.merge!('type' => 'former member') }

      @all_members = @faculty.concat(@students.concat(@former_members))

      # Add authors and (if applicable) author links

      @authors = []

      # Iterate through all of this publication's authors
      for a in @publication['author']
        n = a.first.to_s + " " + a.last.to_s
        s = n.downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')

        p_first = s.split(/\-/).first
        p_last = s.split(/\-/).last

        found = false

        # Check if this author is a member of the site
        for i in @all_members
          sl = i['name'].downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')
          if sl.start_with?(p_first) && sl.end_with?(p_last)
            found = true
            s = sl
            break
          end
        end

        # If the author is a site member, add their name and a link to their page
        # Otherwise leave the link blank (i.e. only show their name)
        if found
          @authors.append(n + "|" + s)
        else
          @authors.append(n + "| ")
        end
      end

      # Finish setting page properties
      # Accessible in Liquid via `page.<property>` (e.g. `page.title`)

      self.data['publication_authors'] = @authors.join(',')

      self.data['publication_doi'] = @publication['doi']
      self.data['publication_photo'] = @publication['image']
      self.data['publication_pdf'] = @publication['pdf']

      self.data['publication_citation'] = @citation
      self.data['publication_bibtex'] = @publication.to_s
      self.data['publication_file'] = File.file?(@customize_dir) ? File.join('_publication', @fname).to_s : ''

      # Finally, set SEO values

      self.data['title'] = "#{@publication['title']} (Publication)"
      self.data['description'] = @citation

      publication_hash = @publication.to_hash

      if publication_hash.key?(:image) && @publication['image'].to_s.length > 0
        self.data['image'] = @publication['image']
      end
    end
  end
end
