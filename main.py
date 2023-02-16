from app import app
from config import db
from models import Item, Order, Customer, Order_detail, Payment, Cash, Check, Credit, Wire_transfer  # , Order_status
from models.Item import Item
from models.Order import Order
from models.Customer import Customer
from models.Order_detail import Order_detail
from models.Payment import Payment
from models.Credit import Credit
from models.Cash import Cash
from models.Check import Check
from models.Wire_transfer import Wire_transfer
from flask import jsonify, render_template, request

with app.app_context():
    # db.drop_all()
    db.create_all()

"""CRUD operations for item"""


@app.route('/item/add', methods=['POST'])
def itemAdd():
    try:
        json = request.json
        print(json)
        weight = json["weight"]
        description = json["description"]

        if weight and description and request.method == 'POST':
            item = Item(weight=weight, description=description)
            print("*******************")

            db.session.add(item)
            db.session.commit()
            response = jsonify('Nouveau item ajouté avec succès')
            return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/items', methods=['GET'])
def items():
    try:
        items = Item.query.all()
        data = [{"weight": item.weight, "description": item.description}
                for item in items]
        print(data)
        response = jsonify({"statut_code": 200, "items": data})
        return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message


@app.route('/item/update', methods=['PUT'])
def itemUpdate():
    try:
        data = request.json
        print(data)
        id = data["id"]
        weight = data["weight"]
        description = data["description"]
        item = Item.query.filter_by(id=id).first()
        print(item)
        if id and weight and description and request.method == 'PUT':
            item.weight = weight
            item.description = description
            db.session.commit()
            response = jsonify(
                'Les informations de l"item ont été modifiées')
            return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/item/delete', methods=['DELETE'])
def deleteItem():
    try:
        json = request.json
        print(json)
        id = json['id']

        item = Item.query.filter_by(id=id).first()
        print(item)
        db.session.delete(item)
        db.session.commit()
        resultat = jsonify('Item supprimé ♠♦')
        return resultat
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message
    finally:
        db.session.rollback()
        db.session.close()


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port="3000")
