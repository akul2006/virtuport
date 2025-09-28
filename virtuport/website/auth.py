from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/home')
def home():
    return render_template("index.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        print(data)

@auth.route('/about')
def about():
    return render_template("about.html")

@auth.route('/accessibility')
def accessibility():
    return render_template("accessibilityinfo.html")

@auth.route('/admissions')
def admissions():
    return render_template("admissions.html")

@auth.route('/contact')
def contact():
    return render_template("contact.html")

@auth.route('/digital_learning')
def digital_learning():
    return render_template("Digital Learning.html")

@auth.route('/faculty_resources')
def faculty_resources():
    return render_template("faculty and staff resources.html")

@auth.route('/curriculum')
def curriculum():
    return render_template("Hands-on Curriculum.html")

@auth.route('/industry_partnership')
def industry_partnership():
    return render_template("industry-partnership.html")

@auth.route('/news_events')
def news_events():
    return render_template("news and event.html")

@auth.route('/programs')
def programs():
    return render_template("programs.html")

@auth.route('/research')
def research():
    return render_template("research and innovation.html")

@auth.route('/social_media')
def social_media():
    return render_template("social media integration.html")

@auth.route('/student_resources')
def student_resources():
    return render_template("Student Resources.html")