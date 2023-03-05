# This is where all the database collections are defined. A collection is a place to hold a defined 
# set of data like Users, Posts, Comments. Collections are defined below as classes. Each class name is 
# the name of the data collection and each item is a data 'field' that stores a piece of data.  Data 
# fields have types like IntField, StringField etc.  This uses the Mongoengine Python Library. When 
# you interact with the data you are creating an onject that is an instance of the class.

from sys import getprofile
from tokenize import String
from typing import KeysView
from xmlrpc.client import Boolean

from setuptools import SetuptoolsDeprecationWarning
from app import app
from flask import flash
from flask_login import UserMixin
from mongoengine import FileField, EmailField, StringField, IntField, ReferenceField, DateTimeField, BooleanField, CASCADE
from flask_mongoengine import Document
from werkzeug.security import generate_password_hash, check_password_hash
import datetime as dt
import jwt
from time import time
#from bson.objectid import ObjectId

class User(UserMixin, Document):
    createdate = DateTimeField(defaultdefault=dt.datetime.utcnow)
    #gid = StringField(sparse=True, unique=True, required=True)
    gid = StringField(sparse=True, unique=True)
    gname = StringField()
    gprofile_pic = StringField()
    isadmin = BooleanField(default=False)
    username = StringField()
    password_hash = StringField()
    fname = StringField()
    lname = StringField()
    email = EmailField()
    image = FileField()
    role = StringField()
    school = StringField()
    pronouns = StringField()
    
    # Below Is teacher only data
    teacher_number = IntField(sparse=True,unique=True)
    troom_number = StringField()
    tdescription = StringField()
    tacademy = StringField()
    tdepartment = StringField()
    troom_phone = IntField()

    # Self-rating
    leniency = IntField()
    empathy = IntField()
    feedback = IntField()
    patience = IntField()
    classcontrol = IntField()

    meta = {
        'ordering': ['lname','fname']
    }
    

class Post(Document):
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    subject = StringField()
    content = StringField()
    tag = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }


# _____________________ iRate

class Courses(Document): 
    course_number = StringField(required=True,unique=True)
    course_title = StringField()
    course_name = StringField()
    course_ag_requirement = StringField()
    course_difficulty = StringField()
    course_department = StringField()
    course_pathway = StringField()
    course_paideia_option = BooleanField()
    course_gradelevel = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class TeacherCourse(Document):
    teachercourseid = StringField(sparse=True, required=True,unique=True)
    teacher = ReferenceField('User',reverse_delete_rule=CASCADE, required=True) 
    course = ReferenceField('Courses',reverse_delete_rule=CASCADE,required=True)
    course_description = StringField()
    course_files = FileField()
    course_link = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()
    is_paideia = BooleanField()

    meta = {
        'ordering': ['-createdate']
    }

    # Refercnce Teacher Class
class Comment(Document):
    # Line 63 is a way to access all the information in Course and Teacher w/o storing it in this class
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    # post = ReferenceField('Post',reverse_delete_rule=CASCADE)
    course = ReferenceField('Courses',reverse_delete_rule=CASCADE)
    # This could be used to allow comments on comments
    # comment = ReferenceField('Comment',reverse_delete_rule=CASCADE)
    # Line 68 is where you store all the info you need but won't find in the Course and Teacher Object
    content = StringField()
    create_date = DateTimeField(default=dt.datetime.utcnow)
    modify_date = DateTimeField()
    role = StringField("Role")

    meta = {
        'ordering': ['-createdate']
    }