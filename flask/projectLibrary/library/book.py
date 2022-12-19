from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from library.auth import login_required
from library.db import get_db

bp = Blueprint('book', __name__)

@bp.route('/')
def index():
    db = get_db()
    books = db.execute(
        'SELECT  title, description,author_id,jenre_id, status_id, jenre.name '
        ' FROM books  JOIN jenre  ON books.jenre_id = jenre.id'
    ).fetchall()
    for i in books:
        print(i['name'])
    return render_template('book/index.html', books=books)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        author_id = request.form['author_id']
        jenre_id = request.form['jenre_id']
        status_id = request.form['status_id']
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
            return redirect(url_for('book.index'))

    return render_template('book/create.html')

@bp.route('/add_jenre', methods=['GET', 'POST'])
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
    return render_template('book/add_jenre.html')


@bp.route('/jenre')
def jenre():
    db = get_db()
    jenres = db.execute(
        'SELECT * '
        ' FROM jenre'
    ).fetchall()
    print(jenres)
    return render_template('book/jenre.html', jenres=jenres)


@bp.route('/add_status', methods=['GET', 'POST'])
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


@bp.route('/status')
def status():
    db = get_db()
    statuses = db.execute(
        'SELECT * '
        ' FROM status'
    ).fetchall()
    return render_template('book/status.html', statuses=statuses)


@bp.route('/add_author', methods=['GET', 'POST'])
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
    return render_template('book/add_author.html')

@bp.route('/author')
def author():
    db = get_db()
    authors = db.execute(
        'SELECT * '
        ' FROM authors'
    ).fetchall()
    return render_template('book/author.html', authors=authors)
