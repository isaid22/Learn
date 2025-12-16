import yaml
from typing import Any, Dict


def read_yaml(path: str) -> Dict[str, Any]:
    """Read a YAML file safely without truncating it.

    Opens the file in read mode and parses it with yaml.safe_load.
    Returns an empty dict if the file is empty or contains no mappings.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data or {}


def write_yaml(path: str, data: Dict[str, Any]) -> None:
    """Write a YAML file safely.

    Opens the file in write mode only when dumping provided data.
    """
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False)


def main() -> Dict[str, Any]:
    filename = "sample_yaml.yaml"

    # Read current config without truncating the file
    config = read_yaml(filename)

    # Example: modify config in-memory, then persist
    if "updated_at" not in config:
        config["updated_at"] = "now"

    # Persist changes
    new_file_name = "sample_yaml_updated.yaml"
    write_yaml(filename, config)
    return config


if __name__ == "__main__":
    my_configurations = main()
    print(my_configurations)
