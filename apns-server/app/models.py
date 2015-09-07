from . import db

class Identity(db.Model):
    __tablename__ = 'identity'
    id = db.Column(db.Integer, primary_key=True)
    identity = db.Column(db.String(64))
    device = db.Column(db.String(64))
    token = db.Column(db.String(64))
    regiseryTime = db.Column(db.DateTime)

    def __repr__(self):
        return '<identity: %r, device: %r, token: %r, update: %>' % \
            (self.identity, self.device, self.token, self.regiseryTime)
