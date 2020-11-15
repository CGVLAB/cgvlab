# Generates a page for each paper
# Pages are located at /paper/<key>/index.html
# Uses the BibTeX file _bibliography/references.bib
# Each page can have customized content by creating a .html file with the papers's key in _include/_paper

require 'bibtex'
require 'citeproc'
require 'csl/styles'

module Jekyll
  class PaperPageGenerator < Generator
    safe true

    def generate(site)
        dir = 'paper'
        bib = BibTeX.open('_bibliography/references.bib')

        cp = CiteProc::Processor.new style: 'modern-language-association', format: 'text'
        cp.import bib.to_citeproc

        for paper in bib
          citation = cp.render :bibliography, id: paper.id
          site.pages << PaperPage.new(site, site.source, File.join(dir, paper.key), paper, citation)
        end
    end
  end

  # A Page subclass used in the `PaperPageGenerator`
  class PaperPage < Page
    def initialize(site, base, dir, paper, citation)
      @site = site
      @base = base
      @dir = dir
      @paper = paper
      @citation = citation

      @name = 'index.html'
      @fname = paper.key + '.html'
      @customize_dir = File.join(base, '_includes', '_paper', @fname);
      
      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'paper.html')

      self.data['title'] = "#{@paper['title']} (Paper) - CGVLab"

      self.data['paper_title'] = @paper['title']
      self.data['paper_year'] = @paper['year']
      self.data['paper_source'] = @paper['booktitle'] || @paper['journal'] || @paper['publisher'] || 'Unknown'

      # Add authors and author links (if applicable)

      @faculty = site.data['faculty'].map{|s| s.merge!('type' => 'faculty') }
      @students = site.data['students'].map{|s| s.merge!('type' => 'student') }
      @former_members = site.data['former_members'].map{|s| s.merge!('type' => 'former member') }

      @all_members = @faculty.concat(@students.concat(@former_members))

      @authors = []

      for a in @paper['author']
        n = a.first.to_s + " " + a.last.to_s
        s = n.downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')

        p_first = s.split(/\-/).first
        p_last = s.split(/\-/).last

        found = false

        for i in @all_members
          sl = i['name'].downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')
          if sl.start_with?(p_first) && sl.end_with?(p_last)
            found = true
            s = sl
            break
          end
        end

        if found
          @authors.append(n + "|" + s)
        else
          @authors.append(n + "| ")
        end
      end

      self.data['paper_authors'] = @authors.join(',')

      self.data['paper_doi'] = @paper['doi']
      self.data['paper_photo'] = @paper['image']
      self.data['paper_pdf'] = @paper['pdf']

      self.data['paper_citation'] = @citation
      self.data['paper_bibtex'] = @paper.to_s
      self.data['paper_file'] = File.file?(@customize_dir) ? File.join('_paper', @fname).to_s : ''
    end
  end
end
