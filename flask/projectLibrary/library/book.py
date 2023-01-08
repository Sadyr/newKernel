from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from library.auth import login_required
from library.db import get_db

bp = Blueprint('book', __name__)

menus = [
        {'name': 'Главная', 'url':"/"},
         {'name': 'Книги', 'url':"/books"},
        {'name': 'Фильмы', 'url':"#"},
    ]


book_list = [
        {'name': 'Название'},
         {'name': 'Описание'},
        {'name': 'Автор'},
        {'name': 'Жанр'},
        {'name': 'Статус'}
    ]




@bp.route('/books')
def books():   # Функция для главной страницы сайта
    db = get_db()
    books = db.execute(
       'SELECT  books.id, title, description,author_id,jenre_id, status_id, jenre.name '
        ' FROM books  JOIN jenre  ON books.jenre_id = jenre.id'
    ).fetchall()
    title = 'Books'
    return render_template('book/books.html',title=title,menus=menus, books=books )

@bp.route('/')
def index():
    title = 'Главная страница'
    
    return render_template('book/index.html', title=title,menus=menus )


@bp.route('/add_book', methods=['GET', 'POST'])  # Функция для добавление книг
@login_required
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        author_id = request.form['author']
        jenre_id = request.form['jenre']
        status_id = request.form['status']
        error = None

        if not title:
            error = 'Title is required.'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO books (title, description, author_id, jenre_id, status_id)'
                ' VALUES (?,?,?,?,?)',
                (title, description, author_id, jenre_id, status_id)
            )
            db.commit()
            return redirect(url_for('book.books'))
    db = get_db()
    authors = db.execute(
        'SELECT * '
        ' FROM authors'
    ).fetchall()
    jenres = db.execute(
        'SELECT * '
        ' FROM jenre'
    ).fetchall()
    statuses = db.execute(
        'SELECT * '
        ' FROM status'
    ).fetchall()

    return render_template('book/add_book.html', authors=authors, jenres = jenres, statuses = statuses, menus=menus)



@bp.route('/books/show_book/<int:book_id>')
@login_required
def show_book(book_id):
    db = get_db()
    book = db.execute(
        'SELECT  books.id as id, title, description, authors.name as author , jenre.name as jenre, status.name as status'
        ' FROM books'
        ' INNER JOIN  authors ON books.author_id = authors.id'
        ' INNER JOIN  jenre ON books.jenre_id = jenre.id'
        ' INNER JOIN  status ON books.status_id = status.id'
        ' WHERE books.id = ?',
        (book_id,)
    ).fetchone()
    return render_template('book/show_book.html', book = book, title = 'Книга', menus=menus ,  zip=zip)

@bp.route('/books/edit_book/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        author_id = request.form['author']
        jenre_id = request.form['jenre']
        status_id = request.form['status']
        error = None

        if not title:
            error = 'Title is required.'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE books'
                ' SET title = ?, description = ?,author_id = ?, jenre_id = ?, status_id = ?'
                ' WHERE id = ?',
                (title, description, author_id, jenre_id, status_id, book_id)
            )
            db.commit()
            return redirect(url_for('book.books'))
    db = get_db()
    book = db.execute(
        'SELECT  title, description, authors.name as author , jenre.name as jenre, status.name as status'
        ' FROM books'
        ' INNER JOIN  authors ON books.author_id = authors.id'
        ' INNER JOIN  jenre ON books.jenre_id = jenre.id'
        ' INNER JOIN  status ON books.status_id = status.id'
        ' WHERE books.id = ?',
        (book_id,)
    ).fetchone()
    authors = db.execute(
    'SELECT * '
    ' FROM authors').fetchall()
    jenres = db.execute('SELECT * '
    ' FROM jenre').fetchall()
    statuses = db.execute(
    'SELECT * '
    ' FROM status').fetchall()
    return render_template('book/edit_book.html', book=book, authors=authors, jenres = jenres, statuses = statuses, menus=menus)

@bp.route('/books/delete_book/<int:book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book_id = book_id
    error = None
    db = get_db()
    db.execute(
        'DELETE'
        ' FROM books '
        ' WHERE id = ?', 
        (book_id,)
    )
    db.commit()
    return redirect(url_for('book.books'))


@bp.route('/add_jenre', methods=['GET', 'POST']) # Функция для добавления жанров
@login_required
def add_jenre():
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Name is required'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO jenre (name)'
                ' VALUES (?)',
                (name,)
            )
            db.commit()
            return redirect(url_for('book.jenre'))
    return render_template('book/add_jenre.html',menus=menus)


@bp.route('/jenre') # Функция страницы жанры
def jenre():
    db = get_db()
    jenres = db.execute(
        'SELECT * '
        ' FROM jenre'
    ).fetchall()
    print(jenres)
    return render_template('book/jenre.html', jenres=jenres, title = 'Jenres',menus=menus)


@bp.route('/add_status', methods=['GET', 'POST'])  # Функция для добавления статуса 
@login_required
def add_status():
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Name is required'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO status (name)'
                ' VALUES (?)',
                (name,)
            )
            db.commit()
            return redirect(url_for('book.status'))
    return render_template('book/add_status.html')


@bp.route('/status') # Функция для страницы статуса
def status():
    db = get_db()
    statuses = db.execute(
        'SELECT * '
        ' FROM status'
    ).fetchall()
    return render_template('book/status.html', statuses=statuses, title = 'Statuses',menus=menus)


@bp.route('/add_author', methods=['GET', 'POST']) # Функция для добавления автора книг
@login_required
def add_author():
    if request.method == 'POST':
        name = request.form['name']
        error = None

        if not name:
            error = 'Name is required'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO authors (name)'
                ' VALUES (?)',
                (name,)
            )
            db.commit()
            return redirect(url_for('book.author'))
    return render_template('book/add_author.html', title = 'Add authors', menus=menus)

@bp.route('/authors')  # Страница для автора книг
def author():
    db = get_db()
    authors = db.execute(
        'SELECT * '
        ' FROM authors'
    ).fetchall()
    return render_template('book/authors.html', authors=authors, menus=menus)
