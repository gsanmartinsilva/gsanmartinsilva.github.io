import os
import jinja2
import yaml

params = yaml.load(open("info.yaml"), Loader=yaml.FullLoader)
basic_info = params['basic_info']
publication_list = params['publication_list']
social = params['social']

environment = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
output_text = environment.get_template('index.html').render(basic_info=basic_info,
                                                            publication_list=publication_list,
                                                            social=social)

with open(os.path.join('rendered_files', 'index.html'), "w") as result_file:
    result_file.write(output_text)