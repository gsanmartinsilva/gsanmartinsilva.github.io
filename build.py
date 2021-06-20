import os
import jinja2
import yaml

render_vars = {
    "greeting": "Oh hi Mark"
}

params = yaml.load(open("info.yaml"), Loader=yaml.FullLoader)


environment = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
output_text = environment.get_template('index.html').render(render_vars)

print(output_text)


with open(os.path.join('rendered_files', 'index.html'), "w") as result_file:
    result_file.write(output_text)