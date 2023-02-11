from sqlalchemy.orm import Session

from . import models, schemasa




# ----------------------------------------------------- Parent User Section --------------------------------------------

def get_parent(db: Session, parent_id: int):
    return db.query(models.Parent).filter(models.Parent.id==parent_id).first()


def get_parents(db: Session, skip: int=0, limit: int = 100):
    try:
        return db.query(models.Parent).offset(skip).limit(limit).all()
    except:
        return []


def create_parent(db: Session, parent: schemasa.ParentCreate):
    db_parent = models.Parent(first_name=parent.first_name, last_name=parent.last_name, address=parent.address)

    try:
        db.add(db_parent)

        db.commit()
        db.refresh(db_parent)

        return {'result': db_parent, 'success': True}

    except:
        return {'result': {}, 'success': False}



def update_parent(db: Session, parent_id: int, parent_update: schemasa.Parent):
    try:
        update_result = db.query(models.Parent).filter_by(id=parent_id).update(dict(parent_update))

        db.commit()

        if update_result==1:
            return {'result': update_result, 'success': True}
        else:
            return {'result': {}, 'success': False}
    except:
        return {'result': {}, 'success': False}


def delete_parent(db: Session, parent_id: int):
    try:
        delete_result = db.query(models.Parent).filter(models.Parent.id==parent_id).delete()
        delete_children = db.query(models.Child).filter(models.Child.parent_id==parent_id).delete()
        # db.delete(delete_result)

        # print("delete_parent children", delete_children)

        # db.delete(delete_result)

        db.commit()

        if delete_result==1:
            return {'success': True}
        else:
            return {'success': False}
    # delete_result = models.Parent.query.filter(models.Parent.id == parent_id).delete()
    except:
        return {'success': False}


# -------------------------------------------------- Child User Section -------------------------------

def get_children(db: Session, skip: int=0, limit: int=100):
    try:
        return db.query(models.Child).offset(skip).limit(limit).all()
    except:
        return []



def create_parent_child(db: Session, child: schemasa.ChildCreate):
    child = dict(child)
    parent = get_parent(db, child['parent_id'])
    
    if parent == None:
        return {'result': {}, 'success': False}
        # return models.Child(first_name='', last_name='', parent_id=0)
    
    db_child = models.Child(first_name=child['first_name'], last_name=child['last_name'], parent_id=child['parent_id'])

    try:
        db.add(db_child)
        db.commit()
        db.refresh(db_child)
        return {"result": db_child, "success": True}
    
    except:
        return {"result": {}, "success": False}


def update_child(db: Session, child_id: int, child_update: schemasa.Child):
    child_update = dict(child_update)
    parent = get_parent(db, child_update['parent_id'])

    if parent==None:
        return {'result': {}, 'success': False}
        # return models.Child(first_name='', last_name='', parent_id=0)

    try:
        update_result = db.query(models.Child).filter_by(id=child_id).update(dict(child_update))

        db.commit()

        if update_result==1:
            return {'result': update_result, 'success': True}
        else:
            return {'result': {}, 'success': False}

    except:
        return {'result': {}, "success": False}


def delete_child(db: Session, child_id: int):
    try:
        delete_result = db.query(models.Child).filter(models.Child.id==child_id).delete()
    
        # db.delete(delete_result)

        # print("delete_result", delete_result)

        # db.delete(delete_result)

        db.commit()

        if delete_result==1:
            return {'success': True}
        else:
            return {'success': False}


    # delete_result = models.Parent.query.filter(models.Parent.id == parent_id).delete()

    except:
        return {'success': False}



if __name__ == "__main__":
    result = Session.query(models.Parent)

    print("result", result)
