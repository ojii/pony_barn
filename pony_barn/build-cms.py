from pony_barn.base_django import DjangoGitBuild
from pony_barn import client as pony
import sys

class PonyBuild(DjangoGitBuild):

    def __init__(self):
        super(PonyBuild, self).__init__()
        self.repo_url = "git://github.com/digi604/django-cms-2.0.git"
        self.name = "cms"
        self.installed_apps = ['cms', 'menus', 'mptt', 'publisher', 'example']
        self.default_db = 'mysql'
        self.required += ['south']
        

    def define_commands(self):
        self.commands = [
            self.vcs_class(self.repo_url, egg=self.get_name()),
            pony.BuildCommand([self.context.python, 'setup.py', 'install'], name='Install'),
            pony.BuildCommand([self.context.djangoadmin, 'syncdb', '--noinput', '--settings', self.settings_path], name='Syncdb'),
            pony.TestCommand([self.context.djangoadmin, 'test', self.get_name(), '--settings', self.settings_path], name='run tests')
            ]

if __name__ == '__main__':
    build = PonyBuild()
    sys.exit(build.execute(sys.argv))