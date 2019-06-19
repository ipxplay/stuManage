from jinja2 import Environment,PackageLoader
def getData(filename="data.csv"):
    datas = []
    with open(filename,encoding="utf-8") as f:
        data = f.readlines()
    for d in data:
        line = d.split(',')
        datas.append(line)
    return datas
env = Environment(loader=PackageLoader(package_name="snifferHosts.render"))
template = env.get_template("data.html")
users = getData()
html = template.render(**locals())
print(html)
