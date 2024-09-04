from flask import Flask, request, jsonify, abort
from models import db, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts])

@app.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({'id': post.id, 'title': post.title, 'content': post.content})

@app.route('/posts', methods=['POST'])
def create_post():
    if not request.json or not 'title' in request.json or not 'content' in request.json:
        abort(400, description="Title and content are required fields.")
    post = Post(title=request.json['title'], content=request.json['content'])
    db.session.add(post)
    db.session.commit()
    return jsonify({'id': post.id, 'title': post.title, 'content': post.content}), 201

@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
