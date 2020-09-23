import os
import re


# 获得根目录
def root_path():
    file_address = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
    root_path = re.search(r'(.*)common', file_address)
    print(root_path.group(1))
    return root_path.group(1)


def std_yaml_path():
    yaml_path = os.path.join(root_path(), 'data/std/data.yaml')
    if not os.path.exists(yaml_path):
        os.mkdir(yaml_path)
    return yaml_path


def std_crg_path():
    crg_path = os.path.join(root_path(), 'data/std/config.ini')
    if not os.path.exists(crg_path):
        os.mkdir(crg_path)
    return crg_path

def log_path():
    log_path = os.path.join(root_path(), 'log/')
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    return log_path


def qhsp_yaml_path():
    yaml_path = os.path.join(root_path(), 'data/qhsp/data.yaml')
    if not os.path.exists(yaml_path):
        os.mkdir(yaml_path)
    return yaml_path


def qhsp_crg_path():
    crg_path = os.path.join(root_path(), 'data/qhsp/config.ini')
    if not os.path.exists(crg_path):
        os.mkdir(crg_path)
    return crg_path


def qhsp_report_path():
    report_path = os.path.join(root_path(), 'qhsp/test_report/')
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    return report_path


def gdzq_yaml_path():
    yaml_path = os.path.join(root_path(), 'data/gdzq/data.yaml')
    if not os.path.exists(yaml_path):
        os.mkdir(yaml_path)
    return yaml_path


def gdzq_crg_path():
    crg_path = os.path.join(root_path(), 'data/gdzq/config.ini')
    if not os.path.exists(crg_path):
        os.mkdir(crg_path)
    return crg_path


def gdzq_report_path():
    report_path = os.path.join(root_path(), 'gdzq/test_report/')
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    return report_path


def yc_yaml_path():
    yaml_path = os.path.join(root_path(), 'data/yc/data.yaml')
    if not os.path.exists(yaml_path):
        os.mkdir(yaml_path)
    return yaml_path


def yc_crg_path():
    crg_path = os.path.join(root_path(), 'data/yc/config.ini')
    if not os.path.exists(crg_path):
        os.mkdir(crg_path)
    return crg_path


def yc_report_path():
    report_path = os.path.join(root_path(), 'yc/test_report/')
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    return report_path


if __name__ == '__main__':
    root_path()
