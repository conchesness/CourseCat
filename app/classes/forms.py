# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask.app import Flask
from flask import flash
from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, NumberRange, Email, Optional, InputRequired, ValidationError, DataRequired, EqualTo
from wtforms import PasswordField, StringField, SubmitField, TextAreaField, HiddenField, IntegerField, SelectField, FileField, BooleanField, IntegerRangeField, URLField
from app.classes.data import User

departments = [("",""),("Mathmatics","Mathmatics"),("Science", "Science"),("English", "English"),("Visual and Performing Arts", "Visual and Performing Arts"),("Humanities", "Humanities"),("PE", "Physical Education (PE)"), ("World Languages", "World Languages"), ("CTE", "Career Techincal Education (CTE)"),("Other Elective","Other Elective")]
pathways = [("",""),("Computer Science","Computer Science"),("Engineering","Engineering"),("FADA","FADA"),("Health","Health"),("Race, Policy and Law","Race, Policy and Law"),("Any","Any")]

class CourseFilterForm(FlaskForm):
    department = SelectField('Department',choices = departments)
    name = StringField('Course Name')
    incomplete = BooleanField('Incomplete')
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
    troom_number = StringField('Room Number')
    tdescription = TextAreaField('Description')
    tacademy = SelectField('Academy', choices=pathways)
    tdepartment = SelectField('Department',choices=departments)
    troom_phone = StringField('Phone Number', validators=[Optional()])
    image = FileField("Image") 
    paideia = BooleanField("Paideia")
    late_work = IntegerRangeField('Late Work')
    late_work_policy = TextAreaField('Late Work Policy', render_kw={"placeholder": "Late Work Policy (optional)"})
    feedback = IntegerRangeField('Openness to Feedback')
    feedback_policy = TextAreaField('Feedback Policy')
    classcontrol = IntegerRangeField('Classroom Environment')
    classcontrol_policy = TextAreaField('Class Control Policy')
    grading_policy = TextAreaField('Grading Policy')
    classroom = TextAreaField('Tell us about your classroom.')
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
    course_gradelevel = SelectField('Grade Level', choices=[("",""),("9th","9th"),("10th","10th"),("11th","11th"),("12th","12th"),("Any","Any")])
    submit = SubmitField('Add Course')

class TeacherCourseForm(FlaskForm):
    teacher = SelectField('Teacher',choices=[],validate_choice=False)
    course = SelectField('Course',choices=[],validate_choice=False)
    course_description = TextAreaField('Course Description')
    is_paideia = BooleanField('Paideia')
    course_link = URLField("Link to syllabus",validators=[(Optional()),URL()], render_kw={"placeholder": "https://..."})
    submit = SubmitField('Submit')

class StudentReviewForm(FlaskForm):
    year_taken = IntegerField("Year You Took the Course",validators=[(InputRequired())])
    late_work = IntegerRangeField("Late Work",validators=[(InputRequired())])
    feedback = IntegerRangeField("Feedback",validators=[(InputRequired())])
    classcontrol = IntegerRangeField("Class Control",validators=[(InputRequired())])
    grading_policy = IntegerRangeField("Grading Policy",validators=[(InputRequired())])
    classroom_environment = IntegerRangeField("Classroom Environment",validators=[(InputRequired())])
    submit = SubmitField('Submit')

