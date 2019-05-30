from jinja2 import Environment,PackageLoader,FileSystemLoader

def html(htmlfile,package_name="SimpleWebServer.web",package_path="views",**kwargs):
    env = Environment(loader=PackageLoader(package_name=package_name,package_path=package_path))
    template = env.get_template(htmlfile)
    return template.render(**kwargs)
    