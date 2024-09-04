from extensions import db  # Use the db instance from extensions

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each post
    title = db.Column(db.String(100), nullable=False)  # Title of the post
    content = db.Column(db.Text, nullable=False)  # Content of the post

    def __repr__(self):
        return f"<Post {self.title}>"
