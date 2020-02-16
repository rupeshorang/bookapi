from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    isbn = db.Column(db.Integer)
    rating = db.Column(db.Float)

    def json(self):
        return {'name': self.name, 'price': self.price, 'rating': self.rating, 'isbn': self.isbn}

    def add_book(_name, _price, _isbn, _rating):
        new_book = Book(name=_name, price=_price, isbn=_isbn, rating=_rating)
        db.session.add(new_book)
        db.session.commit()

    def get_all_books():
        return [Book.json(book) for book in Book.query.all()]

    def get_book(_isbn):
        return Book.json(Book.query.filter_by(isbn=_isbn).first())

    def delete_book(_isbn):
        isDeleted = Book.query.filter_by(isbn=_isbn).delete()
        db.session.commit()
        return bool(isDeleted)

    def update_book_price(_isbn, _price):
        book_to_update = Book.query.filter_by(isbn=_isbn).first()
        book_to_update.price = _price
        db.session.commit()

    def update_book_name(_isbn, _name):
        book_to_update = Book.query.filter_by(isbn=_isbn).first()
        book_to_update.name = _name
        db.session.commit()

    def update_book_rating(_isbn, _rating):
        book_to_update = Book.query.filter_by(isbn=_isbn).first()
        book_to_update.rating = _rating
        db.session.commit()

    def replace_book(_isbn, _price, _name, _rating):
        book_to_replace = Book.query.filter_by(isbn=_isbn).frist()
        book_to_replace.price = _price
        book_to_replace.name = _name
        book_to_replace.rating = _rating
        db.session.commit()

    def __repr__(self):
        book_object = {
            'name': self.name,
            'price': self.price,
            'isbn': self.isbn,
            'rating': self.rating
        }
        return json.dumps(book_object)
