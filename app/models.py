from app import db

class Lesson(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	week = db.Column(db.Integer)
	day = db.Column(db.Integer)
	title = db.Column(db.String(140))
	prezi1 = db.Column(db.String(140))
	prezi2 = db.Column(db.String(140))
	prezi3 = db.Column(db.String(140))
	supplemental1 = db.Column(db.String(140))
	supplemental2 = db.Column(db.String(140))
	supplemental3 = db.Column(db.String(140))
	external_link1 = db.Column(db.String(140))
	external_link2 = db.Column(db.String(140))
	external_link3 = db.Column(db.String(140))
	notes = db.Column(db.Text)
	prezi1_title = db.Column(db.String(140))
	prezi2_title = db.Column(db.String(140))
	prezi3_title = db.Column(db.String(140))
	supplemental1_title = db.Column(db.String(140))
	supplemental2_title = db.Column(db.String(140))
	supplemental3_title = db.Column(db.String(140))
	external_link1_title = db.Column(db.String(140))
	external_link2_title = db.Column(db.String(140))
	external_link3_title = db.Column(db.String(140))


	def __repr__(self):
		return '<Lesson %r>' % (self.id)


class Achievement(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(140))
	category = db.Column(db.String(140))
	number = db.Column(db.Integer)
	description = db.Column(db.Text)

	def __repr__(self):
		return '<Achievement %r>' % (self.name)


class SampleCode(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(140))
	language = db.Column(db.String(60))
	developer_first = db.Column(db.String(60))
	developer_last = db.Column(db.String(60))	
	filename = db.Column(db.String(140))
	docs = db.Column(db.Text)
	description = db.Column(db.Text)

	def __repr__(self):
		return '<Sample_Code %r>' % (self.name)