import os

allrecipes_url_base = "https://www.allrecipes.com/recipes/79/desserts/?page={page}"
jamie_oliver_url_base = "https://www.jamieoliver.com/recipes/category/course/desserts/?rec-page={page}"

allrecipes_filename_base = "allrecipes{:03d}.html"
jamie_oliver_filename_base = "jamie_oliver{:02d}.html"

catalogue_directory = os.path.join("pages", "catalogues")
recipe_directory = os.path.join("pages", "recipes")
