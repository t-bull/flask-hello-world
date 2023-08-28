from ..app import app


class Fruit(app.db.Model):
    __tablename__ = "fruit"
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(50), unique=True, nullable=False)
    weight = app.db.Column(app.db.Integer)
    quantity = app.db.Column(app.db.Integer)

    def __repr__(self):
        return f'<Fruit {self.name}>'
