# Academic website template
This repository contains the code neccesary to build your own **static**, **responsive** and **minimalist** personal landing page. It includes sections to list your bio, your internet links (such as GitHub, Linkedin, etc.), your research and your CV.

It should be fairly easy to extend it with blogging capabilities, but it is not currently implemented because I don't like blogging :yum:.

## How it was made

This project was made using basic `html` and `css` stuff, the jinja2 template engine and Skeleton project to add responsiveness to the website (it looks great on mobile!).


## Why it was made

Nowadays we are mostly interacting with other researchers online. I think it is useful to have a simple and elegant page to present yourself. Think of this as an online business card.

## Instructions.

Ok. It's super simple. It is designed around the idea that you should not touch the `html` or `css` files. The steps are:

1. You put your information in the `info.yaml` file. It should be self-explanatory to fill it.
2. You build the website running the `build.py` file. For this you will need the python library `jinja2` installed. There is a complete list of the environment used for this project inside `requirements.txt`.
3. The final rendered `html` files will be located inside `rendered_files`. You can hang this files inside a webserver to make your webpage available online. I personally recommend using GitHub Pages (it's super simple, google should have all the info you need).


If you have any questions, feel free to contact me 	:wink:. If this was useful for you, stars are appreciated (nothing better than fake internet validation points, you know how it is).




