require "bibtex"
require "citeproc"
require "csl/styles"

module Jekyll
  class PaperPageGenerator < Generator
    safe true

    def generate(site)
        dir = "paper"
        bib = BibTeX.open("_bibliography/references.bib")

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

      @name = "index.html"
      
      self.process(@name)
      self.read_yaml(File.join(base, "_layouts"), "paper.html")

      self.data["title"] = "#{@paper["title"]} (Paper) - CGVLab"

      self.data["paper_title"] = @paper["title"]
      self.data["paper_year"] = @paper["year"]
      self.data["paper_source"] = @paper["booktitle"] || @paper["journal"] || @paper["publisher"] || "Unknown"
      self.data["paper_authors"] = @paper["author"].to_s

      self.data["paper_doi"] = @paper["doi"]
      self.data["paper_photo"] = @paper["image"]
      self.data["paper_pdf"] = @paper["pdf"]

      self.data["paper_citation"] = @citation
      self.data["paper_bibtex"] = @paper.to_s
    end
  end
end
