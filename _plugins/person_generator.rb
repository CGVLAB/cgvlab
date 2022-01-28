# Generates a page for each person
# Pages are located at /team/<name>/index.html
# Each page can have customized content by creating a .html file with the person's slug-ified name in _include/_person

module Jekyll
  class PersonPageGenerator < Generator
    safe true

    def generate(site)
      # Check if the this layout exists
      
      layout = 'person'
      dir = 'team'

      if site.layouts.key? layout

        # Read bibliography
        bib = BibTeX.open('_bibliography/references.bib')

        # Retrieve person types
        faculty = site.data['faculty'].map{|s| s.merge!('type' => 'faculty') }
        students = site.data['students'].map{|s| s.merge!('type' => 'student') }
        former_faculty = site.data['former_faculty'].map{|s| s.merge!('type' => 'former faculty') }
        former_persons = site.data['former_members'].map{|s| s.merge!('type' => 'former member') }

        # Create page for each person
        for person in faculty.concat(students.concat(former_faculty.concat(former_persons)))
          # Create formatted URL
          # https://stackoverflow.com/a/4308399
          formatted_name_url = person['name'].downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')
          # Save page
          site.pages << PersonPage.new(site, site.source, File.join(dir, formatted_name_url), person, formatted_name_url)
        end
      end
    end
  end

  # A Page subclass used in the `PersonPageGenerator`
  class PersonPage < Page
    def initialize(site, base, dir, person, slug)
      # Initialize internal variables
      @site = site
      @base = base
      @dir = dir
      @slug = slug
      @name = 'index.html'

      # Initialize other variables
      @fname = slug + '.html'
      @person = person
      @description = @person['type'].capitalize + (@person['info'].to_s.length > 0 ? ' - ' + @person['info'].to_s : '') 
      @customize_dir = File.join(base, '_pages', '_person', @fname);
      @person_dir = File.join(base, '_layouts', 'person.html')

      # Create file and load layout file
      self.process(@name)
      self.read_yaml(File.dirname(@person_dir), File.basename(@person_dir))

      # Set page properties
      # Accessible in Liquid via `page.<property>` (e.g. `page.title`)

      self.data['person_type'] = @person['type']
      self.data['person_name'] = @person['name']
      self.data['person_bib_query_name'] = @person['bib_query_name']
      self.data['person_photo'] = @person['photo']
      self.data['person_info'] = @person['info']
      self.data['person_url'] = @person['url']
      self.data['person_linkedin'] = @person['linkedin']
      self.data['person_file'] = File.file?(@customize_dir) ? File.join('_person', @fname).to_s : ''

      # Finally, set SEO values

      self.data['title'] = "#{@person['name']} (#{@description})"
      self.data['description'] = @description

      person_hash = @person.to_hash
      
      if person_hash.key?(:photo) && @person['photo'].to_s.length > 0
        self.data['image'] = @person['photo']
      end
    end
  end
end
