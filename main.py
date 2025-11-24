import argparse
from typing import List, Dict, Callable

from functions import create_record, list_records, update_record, remove_record


def main():
    actions: List[str] = ['create', 'list', 'update', 'remove']
    models: List[str] = ['Score', 'Student', 'Group', 'Subject', 'Teacher']

    action_mapper: Dict[str, Callable[[str, int, List[str]], None]] = {
        'create': create_record,
        'list': list_records,
        'update': update_record,
        'remove': remove_record
    }

    parser = argparse.ArgumentParser(
        prog="CRUD Controller",
        description="CRUD operations for various models",
        exit_on_error=False
        )
    parser.add_argument('-a', '--action', choices=actions, required=True, help="CRUD action to perform")
    parser.add_argument('-m', '--model', choices=models, required=True, help="Model to perform the action on")
    parser.add_argument('-id', '--id', type=int, help="id of the model instance")
    parser.add_argument('-r', '--relations', nargs='*', default=[], help="attributes of model's instance in format: attr1 value1 [attr2 value2] ...")

    try:
        args = parser.parse_args()
    except Exception as e:
        print(f"Error parsing arguments: {e}")
    else:
        print("Arguments parsed successfully.")

        action_mapper[args.action](args.model, args.id, args.relations)


if __name__ == "__main__":
    main()
