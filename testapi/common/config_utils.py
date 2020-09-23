import io
import os
import sys
import configparser


class ConfigTools(object):
    def __init__(self, file):
        self.file = file
        self.cp = configparser.ConfigParser()
        try:
            self.cp.read(self.file)
        except:
            self.cp.read(self.file, encoding='utf-8-sig')

    def add_section(self, section):
        self.cp.add_section(section)

    def get_sections(self):
        return self.cp.sections()

    def get_options(self, section):
        return self.cp.options(section)

    def get_items(self, section):
        return dict(self.cp.items(section))

    def get_value(self, section, key):
        return self.cp.get(section, key)

    def get_dumps(self):
        options = self.get_sections()
        key_value = [ ]
        for number in options:
            kv = self.cp.items(number)
            key_value.append(kv)
        return key_value

    def delete_section_item(self, section, key):
        self.cp.remove_option(section, key)

    def delete_section(self, section):
        self.cp.remove_section(section)

    def config_seve(self):
        with open(self.file, 'w') as filepath:
            self.cp.write(filepath)

    def check_have_section(self, section):
        return self.cp.has_section(section)

    def check_have_option(self, section, key):
        return self.cp.has_option(section, key)

