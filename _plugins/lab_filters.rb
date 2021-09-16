# Custom filters used by the site

module Jekyll
    module LabFilters
        # Sort an array of objects using the last name of each object's "name" property
        # (Sorts in ascending order)
        def lab_sort_last_name(obj)
            obj.sort_by{|e| e["name"].split(" ").last()}
        end
    end
end

Liquid::Template.register_filter(Jekyll::LabFilters)
