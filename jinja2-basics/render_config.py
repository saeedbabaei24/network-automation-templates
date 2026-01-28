
from jinja2 import Environment, FileSystemLoader

data = {
    "hostname":"SW-BR-01",
    "interfaces":[
        {"name":"Gig1/0/1", "desc":"POS", "mode":"access","vlan": 10 },
        {"name":"Gig1/0/2", "desc":"POS", "mode":"access","vlan": 10 },
        {"name":"Gig1/0/3", "desc":"POS", "mode":"trunk" },
    ],
}

env = Environment(
    loader=FileSystemLoader("templates"),
    trim_blocks=True,  #removes empty lines
    lstrip_blocks=True   
)

template = env.get_template("switch_interfaces.j2")

rendered = template.render(data)

with open("output/SW-BR-01.cfg", "w") as f:
    f.write(rendered)

print("Configuration generated successfully.")    