import os
import jinja2
import yaml

render_vars = {
    "website_name": "JOOOOLOOO"
}

params = yaml.load(open("info.yaml"), Loader=yaml.FullLoader)

basic_info = params['basic_info']
publication_list = params['publication_list']
print(publication_list)
environment = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
output_text = environment.get_template('index.html').render(basic_info, publication_list=publication_list)



with open(os.path.join('rendered_files', 'index.html'), "w") as result_file:
    result_file.write(output_text)