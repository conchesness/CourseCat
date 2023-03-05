# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask.app import Flask
from flask import flash
from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, NumberRange, Email, Optional, InputRequired, ValidationError, DataRequired, EqualTo
from wtforms.fields.html5 import URLField
from wtforms import PasswordField, StringField, SubmitField, TextAreaField, HiddenField, IntegerField, SelectField, FileField, BooleanField
from app.classes.data import User

departments = [("",""),("Mathmatics","Mathmatics"),("Science", "Science"),("English", "English"),("Visual and Performing Arts", "Visual and Performing Arts"),("Humanities", "Humanities"),("PE", "Physical Education (PE)"), ("World Languages", "World Languages"), ("CTE", "Career Techincal Education (CTE)"),("Other Elective","Other Elective")]
pathways = [("",""),("Computer Science","Computer Science"),("Engineering","Engineering"),("FADA","FADA"),("Health","Health"),("Race, Policy and Law","Race, Policy and Law")]

class CourseFilterForm(FlaskForm):
    department = SelectField('Department',choices = departments)
    submit = SubmitField("Search")

class ProfileForm(FlaskForm):
    pronouns = StringField('Pronouns')
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    role = SelectField('Role',choices=[("Teacher","Teacher"),("Student","Student")])
    school = SelectField('School',choices=[("Oakland Technical High School","Oakland Technical High School")])
    image = FileField("Image") 
    submit = SubmitField('Post')

onetoten = [(0,"---"),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)]
class TeacherForm(FlaskForm):
    pronouns = StringField('Pronouns')
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    teacher_number = IntegerField('Teacher Number')
    troom_number = StringField('Room Number')
    tdescription = TextAreaField('Description')
    tacademy = SelectField('Academy', choices=pathways)
    tdepartment = SelectField('Department',choices=departments)
    troom_phone = StringField('Phone Number', validators=[Optional()])
    image = FileField("Image") 
    leniency = SelectField('Leniency', choices=[(0,"---"),(1,"No late work"),(2,"Late work with penalties"),(3,"Late work allowed")])
    empathy = SelectField('Empathy',choices=onetoten)
    feedback = SelectField('Openness to Feedback',choices=[(0,"---"),(1,"No feedback"),(2,"Willing to receive feedback"),(3,"Feedback actively sought")])
    patience = SelectField('Patience', choices=onetoten)
    classcontrol = SelectField('Classroom Environment',choices=[(0,"---"),(1,"Noisey/Chaotic"),(2,"infrequently quiet/Controlled"),(3,"Controlled chaos"),(4,"Usually quiet/Controlled"),(5,"Always quite/Controlled")])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Post', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class CoursesForm(FlaskForm):
    course_number = StringField('Course Number')
    course_title = StringField('Course Title')
    course_name = StringField('Course Name', validators=[DataRequired()])
    course_ag_requirement = SelectField('Courses A-G Requirement',choices=[("",""),("A-History","A-History"),("B-English", "B-English"), ("C-Mathematics","C-Mathematics"), ("D-Science","D-Science"), ("E-Language Other Than English","E-Language Other Than English"), ("F-Visual And Performing Arts","F-Visual And Performing Arts"), ("G-College-Preparatory Elective","G- College-Preparatory Elective")])
    course_difficulty = SelectField('Course Difficulty',choices=[("",""),("AP","Advanced Placement (AP)"),("HP", "Honors (HP)"),("CP","College Prep (CP)")])
    course_difficulty = SelectField('Course Difficulty',choices=[("",""),("AP","Advanced Placement (AP)"),("HP", "Honors (HP)"),("CP","College Prep (CP)")])
    course_department = SelectField('Course Department',choices=departments)
    course_pathway = SelectField('Course Pathway', choices=pathways)
    course_paideia_option = BooleanField('Paideia Option')
    course_gradelevel = SelectField('Grade Level', choices=[("",""),("9th","9th"),("10th","10th"),("11th","11th"),("12th","12th")])
    submit = SubmitField('Add Course')

class TeacherCourseForm(FlaskForm):
    teacher = SelectField('Teacher',choices=[],validate_choice=False)
    course = SelectField('Course',choices=[],validate_choice=False)
    course_description = TextAreaField('Course Description')
    is_paideia = BooleanField('Paideia')
    course_link = URLField("A link to a Google Document or a folder",validators=[(Optional()),URL()])
    submit = SubmitField('Submit')

# Start building out the physical forms. Follow the process you used to create the school tag


