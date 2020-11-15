# Generates a page for each person
# Pages are located at /person/<name>/index.html
# Each page can have customized content by creating a .html file with the person's slug-ified name in _include/_person

module Jekyll
  class PeoplePageGenerator < Generator
    safe true

    def generate(site)
      if site.layouts.key? 'person'

        dir = 'person'
        bib = BibTeX.open('_bibliography/references.bib')

        faculty = site.data['faculty'].map{|s| s.merge!('type' => 'faculty') }
        students = site.data['students'].map{|s| s.merge!('type' => 'student') }
        former_members = site.data['former_members'].map{|s| s.merge!('type' => 'former member') }

        for person in faculty.concat(students.concat(former_members))
          # https://stackoverflow.com/a/4308399
          formatted_name_url = person['name'].downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')
          site.pages << PeoplePage.new(site, site.source, File.join(dir, formatted_name_url), person, formatted_name_url)
        end
      end
    end
  end

  # A Page subclass used in the `PeoplePageGenerator`
  class PeoplePage < Page
    def initialize(site, base, dir, person, slug)
      @site = site
      @base = base
      @dir = dir
      @person = person
      @slug = slug

      @name = 'index.html'
      @fname = slug + '.html'
      @customize_dir = File.join(base, '_includes', '_person', @fname);

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'person.html')

      self.data['title'] = "#{@person['name']} (#{@person['type'].capitalize}) - CGVLab"

      self.data['person_type'] = @person['type']
      self.data['person_name'] = @person['name']
      self.data['person_photo'] = @person['photo']
      self.data['person_info'] = @person['info']
      self.data['person_url'] = @person['url']
      self.data['person_linkedin'] = @person['linkedin']
      self.data['person_file'] = File.file?(@customize_dir) ? File.join('_person', @fname).to_s : ''
    end
  end
end
