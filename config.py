import os

path = os.getcwd()

class BaseConfig(object):
	SECRET_KEY = 'never-commit-secret-key-to-github'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	MAIL_SERVER = 'localhost'
	MAIL_PORT = 1025
	# MAIL_USE_TLS = True
	MAIL_USERNAME = 'support@tickette.com'
	MAIL_PASSWORD = ''

	MAX_CONTENT_LENGTH = 4 * 1024 * 1024

	PROFILE_DIR = os.path.join(path, 'app/static/uploads/profiles')

class TestConfig(BaseConfig):
	DEBUG = True
	TESTING = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevelopmentConfig(BaseConfig):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://admin:admin@localhost/tickette'

class ProductionConfig(BaseConfig):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'postgresql://pnzzqvamgfmnvk:3d64fa63c6c9adcf8dd6add1ae9658e7a05b06b70cd7c39f249d21110942bcca@ec2-34-231-177-125.compute-1.amazonaws.com:5432/dofaq6qsav20s'