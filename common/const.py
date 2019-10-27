import os

allrecipes_url_base = "https://www.allrecipes.com/recipes/79/desserts/?page={page}"
jamie_oliver_url_base = "https://www.jamieoliver.com/recipes/category/course/desserts/?rec-page={page}"

allrecipes_recipe_link_selector = 'article.fixed-recipe-card div.fixed-recipe-card__info > a'
jamie_oliver_recipe_link_selector = 'div.recipe-block > a'

allrecipes_filename_base = "allrecipes{:03d}.html"
jamie_oliver_filename_base = "jamie_oliver{:02d}.html"

allrecipes_recipe_filename_base = "allrecipes_recipe_{:05d}.html"
jamie_oliver_recipe_filename_base = "jamie_oliver_recipe_{:03d}.html"

catalogue_directory = os.path.join("pages", "catalogues")
recipe_directory = os.path.join("pages", "recipes")

data_directory = "data"

allrecipes_recipe_links_json = "allrecipes_links.json"
jamie_oliver_recipe_links_json = "jamie_oliver_links.json"
