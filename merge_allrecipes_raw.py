import json

from common import const, tools

ll = list()
for i in range(14):
    ll.extend(json.loads(tools.load(
        const.data_directory,
        const.allrecipes_recipe_raw_data_json_base.format(i)
    )))
tools.save(json.dumps(ll, indent=4, ensure_ascii=False),
           const.data_directory, const.allrecipes_recipe_raw_data_json)
