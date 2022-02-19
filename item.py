from models.repositories import ItemRepo
from schemas.schemas import ItemSchema
from flask import request
from db import db
from datetime import datetime


itemRepo = ItemRepo()
itemSchema = ItemSchema()
itemListSchema = ItemSchema(many=True)
ITEM_NOT_FOUND = "Item not found for id: {}"


def get(id):
    item_data = itemRepo.fetchById(id)
    if item_data:
        return itemSchema.dump(item_data)
    return {'message': ITEM_NOT_FOUND.format(id)}, 404


def update(id):
    item_data = itemRepo.fetchById(id)
    item_req_json = request.get_json()
    if item_data:
        item_data.Checked = item_req_json['Checked']
        item_data.Name = item_req_json['Name']
        item_data.ItemType = item_req_json['ItemType']
        item_data.Age = item_req_json['Age']
        item_data.Description = item_req_json['Description']
        item_data.ItemDate = datetime.strptime(item_req_json['ItemDate'], '%Y-%m-%d').date()
        itemRepo.update(item_data)
        return itemSchema.dump(item_data)
    return {'message': ITEM_NOT_FOUND.format(id)}, 404


def delete(id):
    item_data = itemRepo.fetchById(id)
    if item_data:
        itemRepo.delete(id)
        return {'message': 'Item deleted successfully'}, 200
    return {'message': ITEM_NOT_FOUND.format(id)}, 404


def create():
    item_req_json = request.get_json()
    item_data = itemSchema.load(item_req_json, session=db.session)
    itemRepo.create(item_data)
    return itemSchema.dump(item_data),201


def getAll():
    return itemListSchema.dump(itemRepo.fetchAll()), 200