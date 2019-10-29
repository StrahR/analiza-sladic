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

allrecipes_recipe_raw_data_json = "allrecipes_raw_{:02d}.json"
jamie_oliver_recipe_raw_data_json = "jamie_oliver_raw.json"


allrecipes_selectors = [
    ('name', 'h1[itemprop="name"]',
     lambda v: v[0].text.strip() if v else None),
    ('desc', 'div[itemprop="description"]',
     lambda v: v[0].text.strip() if v else None),
    ('rating', 'div.recipe-summary__stars > span.aggregate-rating',
        lambda v: {
            'value': v[0].select('meta')[0].get('content') if v else None,
            'count': v[0].select('meta')[1].get('content') if v else None,
        }),
    ('made-it', 'span.made-it-count',
     lambda v: v[0].next.text.split('\xa0')[0] if v else None),
    ('reviews', 'span.review-count',
     lambda v: v[0].text.split()[0] if v else None),
    ('photos', 'span.picture-count-link',
     lambda v: v[0].text.split()[0] if v else None),
    ('ingredients', 'ul.dropdownwrapper > li.checkList__line > label > span',
     lambda v: [val.text for val in v][:-1]),
    ('time', 'li.prepTime__item',
     lambda v: [val.time.get('datetime') for val in v[1:]]),
    ('servings', 'input#servings', lambda v: v[0].get('value') if v else None),
    ('cals', 'span.calorie-count > span:first-child',
     lambda v: v[0].text if v else None),
    ('steps', 'ol.recipe-directions__list > li.step > span.recipe-directions__list--item',
     lambda v: [val.text.strip() for val in v[:-1]]),
    ('nutrition', 'section.recipe-footnotes',
     lambda v: {val.get('itemprop'): val.text.split()[0] for val in v}),
]

jamie_oliver_selectors = [
    ('name', 'div.single-recipe-details > h1',
     lambda v: v[0].text.strip() if v else None),
    ('subheading', 'div.single-recipe-details > p.subheading',
     lambda v: v[0].text.strip() if v else None),
    ('desc', 'head > meta[name="description"]',
     lambda v: v[0].get('content') if v else None),
    ('quote', 'div.recipe-intro', lambda v: v[0].text.strip() if v else None),
    ('servings', 'div.recipe-detail.serves',
     lambda v: v[0].contents[2].strip() if v else None),
    ('time', 'div.recipe-detail.time',
     lambda v: v[0].contents[2].strip() if v else None),
    ('difficulty', 'div.recipe-detail.difficulty',
     lambda v: v[0].contents[2].strip() if v else None),
    ('tags', 'div.tags-list > a', lambda v: [val.text.strip() for val in v]),
    ('category', 'head > link[rel="canonical"]',
     lambda v: v[0].get('href').split('/')[4] if v else None),
    ('nutrition', 'div.nutrition-expanded > ul > li',
     lambda v: {val.select_one('span.title').text.strip():
                (val.select_one('span.top').text.strip(),
                 val.select_one('span.bottom').text.strip()) for val in v}),
    ('ingredients', 'ul.ingred-list > li',
     lambda v: [' '.join(val.text.split()).replace(' ,', ' ').replace('  ', ' ') for val in v]),
    ('steps', 'ol.recipeSteps > li', lambda v: [val.text for val in v]),
    ('tips', 'div.tip > p', lambda v: v[0].text.strip() if v else None),
    ('diets', 'ul.special-diets-list > li > a > span.full-name',
     lambda v: [val.text for val in set(v)]),
]
