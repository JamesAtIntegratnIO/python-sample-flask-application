from db import db
from datetime import date


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    Checked = db.Column(db.Boolean, nullable=False, default=False)
    Name = db.Column(db.String(80), nullable=True, default='')
    ItemType = db.Column(db.String(80), nullable=True, default='')
    Age = db.Column(db.Integer, nullable=True)
    Description = db.Column(db.String(200), nullable=True, default='')
    ItemDate = db.Column(db.Date, nullable=True, default=date.today())


    def __repr__(self):
        return 'ItemModel(Id=%d, Checked=%s, Name=%s, Type=%s, Age=%d, Description=%s, Date=%s, )' % \
               (self.id, self.Checked, self.Name, self.ItemType, self.Age, self.Description, self.ItemDate)

    def json(self):
        return {'id': self.id,
                'Checked': self.Checked,
                'Name': self.Name,
                'ItemType': self.ItemType,
                'Age': self.Age,
                'Description': self.Description,
                'ItemDate': self.ItemDate}
