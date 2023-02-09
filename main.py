from app import app
from config import db
from models import Credit, Item, Order, Customer, Order_detail,Payment, Cash, Check, Credit, Wire_transfer#, Order_status
from flask import jsonify, render_template, request

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()

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
        data = [{"weight": item.weight, "description": item.description} for item in items]
        print(data)
        response = jsonify({"statut_code": 200, "items": data})
        return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message


if (__name__ == '__main__'):
    app.run(host="0.0.0.0", port="3000")
