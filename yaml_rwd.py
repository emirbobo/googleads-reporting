import yaml


def read(file_path):
    with open(file_path, "r") as yaml_file:
        yaml_obj = yaml.safe_load(yaml_file.read())
        return yaml_obj
    return None


def update_yaml(file_path, data):
    with open(file_path, "w") as yaml_file:
        yaml.dump(data, yaml_file)

