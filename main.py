import argparse
from typing import List, Dict, Callable

from functions import create_record, list_records, update_record, remove_record

# from models import Score, Student, Group, Subject, Teacher
# from connect import session

# class_mapping: Dict[str, Callable] = {
#     'Score': Score,
#     'Student': Student,
#     'Group': Group,
#     'Subject': Subject,
#     'Teacher': Teacher
# }

# def create_record(model: str, id: int, name: str, relations: List[str]):

#     # Validate that id is not provided
#     if name is None:
#         print("Error: 'create' action requires the name argument.")
#         return None

#     # Check for existing record with the same name
#     if session.query(class_mapping[model]).filter_by(name=name).first():
#         print(f"{model} with name '{name}' already exists.")
#         return None

#     # Create a new record instance
#     print(f"Creating record for model {model} with name: {name} and relations: {relations}")
#     record = class_mapping[model](name=name)

#     # Set related model attributes if provided
#     if relations:

#         # Ensure relations are in pairs
#         if len(relations) % 2 != 0:
#             print("Error: relations should be in pairs of attribute and value.")
#             return None
        
#         for rel in relations[::2]:
#             if hasattr(record, rel):
#                 setattr(record, rel, int(relations[relations.index(rel) + 1]))
#             else:
#                 print(f"Error: {model} has no attribute '{rel}'")
#                 return None

#     # Attempt to add and flush the new record to catch any integrity errors
#     try:
#         session.add(record)
#         session.flush()
#     except Exception as e:
#         session.rollback()
#         print(f"Error of related models' field(s): {e.__cause__}")
#         return None
    
#     # Commit the new record to the database
#     session.commit()
#     print(f"Record created: {record}")


# def list_records(model: str, id: int, name: str, relations: List[str]):

#     # Validate that only model is provided
#     if id or name or relations:
#         print("'list' action accepts the model argument only.")
#         return None
    
#     print(f"Listing records for model {model}")
#     records = session.query(class_mapping[model]).all()
#     for record in records:
#         print(record)
#     return records


# def update_record(model: str, id: int, name: str, relations: List[str]):

#     # Validate that id is provided
#     if not id:
#         print("Error: 'update' action requires the id argument.")
#         return None
    
#     # Validate that at least one of name or relations is provided
#     if not name and not relations:
#         print("Error: 'update' action requires at least one of name or relations to update.")
#         return None

#     print(f"Updating record for model {model} with id: {id}, name: {name}")
#     target = session.get(class_mapping[model], id)

#     # Check if the record exists
#     if not target:
#         print(f"No {model} found with id: {id}")
#         return None
    
#     if name:
#         target.name = name

#     if relations:
#         # print(f"With relations: {relations}")
#         # Ensure relations are in pairs
#         if len(relations) % 2 != 0:
#             print("Error: relations should be in pairs of attribute and value.")
#             return None

#         attr_dict = {}
#         for rel in relations[::2]:
#             attr_dict[rel] = int(relations[relations.index(rel) + 1])

#             # Check if the attribute exists on the model
#             if not hasattr(target, rel):
#                 print(f"Error: {model} has no attribute '{rel}'")
#                 return None
            
#             setattr(target, rel, attr_dict[rel])
#         print(f"Attributes to update: {attr_dict}")
#     session.commit()
#     print(f"Record updated: {target}")


# def remove_record(model: str, id: int, name: str, relations: List[str]):

#     # Validate that only model and id are provided
#     if name or relations:
#         print("Error: 'remove' action accepts the model and the id arguments only.")
#         return None
    
#     if not id:
#         print("Error: 'remove' action requires the id argument.")
#         return None
    
#     print(f"Removing record for model {model} with id: {id}")
#     target = session.get(class_mapping[model], id)

#     # Check if the record exists
#     if not target:
#         print(f"Error: no record found with id: {id}")
#         return None
    
#     # Delete the record from the session and commit the transaction
#     session.delete(target)
#     session.commit()
#     print(f"Record with id: {id} removed.")
#     return target


def main():
    actions: List[str] = ['create', 'list', 'update', 'remove']
    models: List[str] = ['Score', 'Student', 'Group', 'Subject', 'Teacher']

    action_mapper: Dict[str, Callable[[str, int, str, List[str]], None]] = {
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
    parser.add_argument('-n', '--name', type=str, help="name of the model instance")
    parser.add_argument('-r', '--relations', nargs='*', default=[], help="related models' fields")

    try:
        args = parser.parse_args()
    except Exception as e:
        print(f"Error parsing arguments: {e}")
    else:
        print("Arguments parsed successfully.")
    
    
    
        # for arg in vars(args):
        #     print(f"{arg}: {getattr(args, arg)}")

        # print(args)
        # print(type(args))
        print(vars(args))

        action_mapper[args.action](args.model, args.id, args.name, args.relations)

        # if args.action == 'create':
        #     create_record(args.model, args.id, args.name, args.relations)
        # elif args.action == 'list':
        #     list_records(args.model, args.id, args.name, args.relations)
        # elif args.action == 'update':
        #     update_record(args.model, args.id, args.name, args.relations)
        # elif args.action == 'remove':
        #     print("Remove action selected. Functionality not yet implemented.")

if __name__ == "__main__":
    main()
