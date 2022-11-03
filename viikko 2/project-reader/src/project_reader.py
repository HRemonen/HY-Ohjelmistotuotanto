from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def parse_dependencies(self, deps):
        return list(deps.keys())

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_toml = toml.loads(content)["tool"]["poetry"]
        
        name = parsed_toml["name"]
        description = parsed_toml["description"]
        dependencies = self.parse_dependencies(parsed_toml["dependencies"])
        dev_dependencies = self.parse_dependencies(parsed_toml["dev-dependencies"])


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)