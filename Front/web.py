import sys
sys.path.append('.')
from flask import Flask, render_template, request
from Back.controller.controller_categories import *
from Back.controller.controller_logs import *
from Back.controller.controller_marketplaces import *
from Back.controller.controller_products import *
from Back.controller.controller_sellers import *
from Back.models.model_marketplaces import Marketplace
from Back.models.model_sellers import Seller
from Back.models.model_products import Product
from Back.models.model_categories import Category


if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    @app.route('/')
    def index() -> None:
        return render_template('index.html')

    @app.route('/insert_category')
    def category_created():
        if request.args:
            name = request.args.get('name')
            description = request.args.get('description')
            category = Category(name, description)
            save_cat(category)
            saved = "Category"
            return render_template("inserted.html", saved=saved)
        return render_template('insert_category.html')

    @app.route('/update_category')
    def update_category():
        msg = ''
        if request.args:
            id = request.args.get('id')
            name = request.args.get('name')
            description = request.args.get('description')
            if id is not None and name is None:
                category = list_cat_byId(id)
                return render_template("update_category.html", id_=id, name_=category.name, description_=category.description)
            category = Category(name, description, id)
            if update_cat(category):
                msg = "Categoria atualizada com sucesso!"
                return render_template("update_category.html", message=msg)
            else:
                msg = "Ops, tivemos um problema. Tente novamente mais tarde!"
                return render_template("update_category.html", message=msg)
        return render_template("update_category.html")

    @app.route('/list_categories')
    def list_categories():
        msg = ''
        if request.args:
            id = request.args.get('id')
            if id is not None:
                if delete_cat(id):
                    msg = "Categoria deletada com sucesso!"
                else:
                    msg = "Ops, tivemos um problema. Tente novamente mais tarde!"
        categories = list_cat()
        return render_template("list_categories.html", categories=categories, message=msg)

    @app.route('/list_logs')
    def listed_log():
        list_log = list_l()
        return render_template('list_logs.html', list=list_log)

    @app.route('/insert_marketplace')
    def insert_marketplace():
        if request.args:
            input_name = request.args.get('input_name')
            input_description = request.args.get('input_description')
            marketplace = Marketplace(input_name, input_description)
            save_mkp(marketplace)
            saved = "Marketplaces"
            return render_template("inserted.html", saved=saved)
        return render_template('insert_marketplace.html')

    @app.route('/list_mktplaces')
    def list_mktplaces():
        mktplaces = list_mkp()
        return render_template("list_mktplaces.html", mktplaces=mktplaces)

    @app.route('/insert_product')
    def insert_product():
        if request.args:
            input_name = request.args.get('input_name')
            input_description = request.args.get('input_description')
            input_price = request.args.get('input_price')
            product = Product(input_name, input_description, input_price)
            save_prod(product)
            saved = "Product"
            return render_template("inserted.html", saved=saved)
        return render_template('insert_product.html')

    @app.route('/list_products')
    def list_products():
        products_list = list_prod()
        return render_template("list_products.html", products=products_list)

    @app.route("/insert_seller")
    def insert_sellers():
        if request.args:
            input_name = request.args.get('name')
            input_phone = request.args.get('phone')
            input_email = request.args.get('email')
            seller = Seller(input_name, input_phone, input_email)
            save_sell(seller)
            saved = "Seller"
            return render_template('inserted.html', saved=saved)
        return render_template("insert_seller.html")

    @app.route("/list_sellers")
    def list_sellers():
        sellers = list_sell()
        return render_template("list_sellers.html", sellers=sellers)

    @app.route('/inserted')
    def inserted():
        return render_template("inserted.html", saved=saved)

    app.run(debug=True)
