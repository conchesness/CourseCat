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
    leniency = SelectField('Late Work', choices=[(0,"---"),(1,"No late work"),(2,"In some specific circumstances"),(3,"Late work w/ 50% or more penalty"),(4,"Late work less than 50% penalty"),(5,"Late work allowed")])
    empathy = SelectField('Grading Flexibility',choices=[(0,"---"),(1,"Students' personal situations do not impact grades"),(2,"Students' personal situations can impact grades with confirmation from an adult."),(3,"Students' personal situations can impact grades if students opens a conversation before there is an issue with their grade."),(4,"Students' personal situations can impact grades if the student opens a conversation."),(5,"Teacher works to monitor students emotions and ask questions and uses the information in making decisions about grades.")])
    feedback = SelectField('Openness to Feedback',choices=[(0,"---"),(1,"No feedback"),(2,"Only if prompted by teacher."),(3,"If the student feels uncomfortable/attacked"),(4,"Willing to receive feedback any time"),(5,"Feedback actively sought.")])
    patience = SelectField('Patience', choices=[(0,"---"),(1,"No tolerance policy for disruptions, distractions, bad behavior"),(2,"1 warning before referral to admin or grade penalty"),(3,"Several warnings before referral to admin or grade penalty"),(4,"Teacher works with disruptive students to address issues."),(5,"Teacher works to build productive relationships with students and actively engages in their personal growth.")])
    classcontrol = SelectField('Classroom Environment',choices=[(0,"---"),(1,"Noisy or Chaotic"),(2,"Mostly noisy or chaotic"),(3,"Noisy but not chaotic"),(4,"Mostly Quiet/Controlled"),(5,"Always Quite/Controlled")])
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
    course_gradelevel = SelectField('Grade Level', choices=[("",""),("9th","9th"),("10th","10th"),("11th","11th"),("12th","12th")])
    submit = SubmitField('Add Course')

class TeacherCourseForm(FlaskForm):
    teacher = SelectField('Teacher',choices=[],validate_choice=False)
    course = SelectField('Course',choices=[],validate_choice=False)
    course_description = TextAreaField('Course Description')
    is_paideia = BooleanField('Paideia')
    course_link = URLField("Link to syllabus",validators=[(Optional()),URL()], render_kw={"placeholder": "https://..."})
    submit = SubmitField('Submit')



