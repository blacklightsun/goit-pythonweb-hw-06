from typing import List, Dict, Callable

from models import Score, Student, Group, Subject, Teacher
from connect import session

class_mapping: Dict[str, Callable] = {
    'Score': Score,
    'Student': Student,
    'Group': Group,
    'Subject': Subject,
    'Teacher': Teacher
}

def create_record(model: str, id: int, relations: List[str]):

        # Validate that relations is provided
    if not relations:
        print("Error: no relations provided")
        return None

    # Ensure relations are in pairs
    if len(relations) % 2 != 0:
        print("Error: relations should be in pairs of attribute and value.")
        return None
    
    # Check for existing record with the same name
    attr_dict = {}
    for rel in relations[::2]:
        if rel not in (class_mapping[model]).__mapper__.columns:
            print(f"Error: {model} has no attribute '{rel}'")
            return None
        attr_dict[rel] = relations[relations.index(rel) + 1]

    if session.query(class_mapping[model]).filter_by(**attr_dict).first():
        print(f"{model} with same relations '{attr_dict}' already exists.")
        return None
    
    # Create a new record instance
    print(f"Creating record for model {model} with relations: {relations}")
    record = class_mapping[model]()
    for rel in relations[::2]:
        setattr(record, rel, relations[relations.index(rel) + 1])

    # Attempt to add and flush the new record to catch any integrity errors
    try:
        session.add(record)
        session.flush()
    except Exception as e:
        session.rollback()
        print(f"Error of related models' field(s): {e.__cause__}")
        return None
    
    # Commit the new record to the database
    session.commit()
    print(f"Record created: {record}")


def list_records(model: str, id: int, relations: List[str]):

    # Validate that only model is provided
    if id or relations:
        print("'list' action accepts the model argument only.")
        return None
    
    print(f"Listing records for model {model}")
    records = session.query(class_mapping[model]).all()
    for record in records:
        print(record)
    return records


def update_record(model: str, id: int, relations: List[str]):

    # Validate that at least one of name or relations is provided
    if not relations:
        print("Error: 'update' action requires at least one of relations to update.")
        return None
    
    # Validate that id is provided
    if not id:
        print("Error: 'update' action requires the id argument.")
        return None

    print(f"Updating record for model {model} with id: {id}")
    target = session.get(class_mapping[model], id)

    # Check if the record exists
    if not target:
        print(f"No {model} found with id: {id}")
        return None

    # Ensure relations are in pairs
    if len(relations) % 2 != 0:
        print("Error: relations should be in pairs of attribute and value.")
        return None

    attr_dict = {}
    for rel in relations[::2]:
        if rel not in (class_mapping[model]).__mapper__.columns:
            print(f"Error: {model} has no attribute '{rel}'")
            return None
        attr_dict[rel] = int(relations[relations.index(rel) + 1])
        setattr(target, rel, attr_dict[rel])
    print(f"Attributes to update: {attr_dict}")

    # Attempt to commit the updated record to catch any integrity errors
    try:
        session.commit()
        print(f"Record updated: {target}")
    except Exception as e:
        session.rollback()
        print(f"Error of related models' field(s): {e.__cause__}")
        return None


def remove_record(model: str, id: int, relations: List[str]):

    # Validate that only model and id are provided
    if relations:
        print("Error: 'remove' action accepts the model and the id arguments only.")
        return None
    
    if not id:
        print("Error: 'remove' action requires the id argument.")
        return None
    
    print(f"Removing record for model {model} with id: {id}")
    target = session.get(class_mapping[model], id)

    # Check if the record exists
    if not target:
        print(f"Error: no record found with id: {id}")
        return None
    
    # Delete the record from the session and commit the transaction
    session.delete(target)
    session.commit()
    print(f"Record with id: {id} removed.")
    return target