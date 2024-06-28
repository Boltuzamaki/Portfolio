from flask import Flask, render_template
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__, static_folder="assets", template_folder="templates")


# Dummy data to simulate MongoDB data
experiences = [
    {
        "date": "2015-Present",
        "title": "Rainbow - Themes",
        "subtitle": "Co-Founder, Web Designer & Developer",
        "description": "Reinvetning the way you create websites",
        "image": "assets/images/portfolio/portfolio-01.jpg",
    },
    {
        "date": "2015-Present",
        "title": "App Development",
        "subtitle": "Co-Founder, Web Designer & Developer",
        "description": "Reinvetning the way you create websites",
        "image": "assets/images/portfolio/portfolio-02.jpg",
    },
    {
        "date": "2015-Present",
        "title": "Application Management",
        "subtitle": "Co-Founder, Web Designer & Developer",
        "description": "Reinvetning the way you create websites",
        "image": "assets/images/portfolio/portfolio-03.jpg",
    },
]


education = [
    {
        "date": "2015-Present",
        "title": "Software Develop.",
        "subtitle": "PhD in Software Development",
        "description": "Advanced studies in software development.",
        "image": "assets/images/portfolio/portfolio-04.jpg",
    },
    {
        "date": "2012-2015",
        "title": "Web Design",
        "subtitle": "Master's in Web Design",
        "description": "In-depth knowledge of modern web design.",
        "image": "assets/images/portfolio/portfolio-05.jpg",
    },
]


portfolio = [
    {
        "category": "PHOTOSHOP",
        "likes": 650,
        "title": "The services provide for design",
        "image": "assets/images/portfolio/portfolio-06.jpg",
    },
    {
        "category": "Figma",
        "likes": 650,
        "title": "Mobile app landing design & Services",
        "image": "assets/images/portfolio/portfolio-05.jpg",
    },
    {
        "category": "Laravel",
        "likes": 650,
        "title": "Web app Responsive design & Services",
        "image": "assets/images/portfolio/portfolio-04.jpg",
    },
    {
        "category": "Figma",
        "likes": 650,
        "title": "PHP with app landing design & Services",
        "image": "assets/images/portfolio/portfolio-03.jpg",
    },
]

resume = {
    "education": [
        {
            "title": "Personal Portfolio April Fools",
            "institution": "University of DVI",
            "period": "1997 - 2001",
            "grade": "4.30/5",
            "description": "The education should be very interactual. Ut tincidunt est ac dolor aliquam sodales. Phasellus sed mauris hendrerit, laoreet sem in, lobortis mauris hendrerit ante.",
        },
        {
            "title": "Examples Of Personal Portfolio",
            "institution": "College of Studies",
            "period": "2000 - 2002",
            "grade": "4.50/5",
            "description": "Maecenas finibus nec sem ut imperdiet. Ut tincidunt est ac dolor aliquam sodales. Phasellus sed mauris hendrerit, laoreet sem in, lobortis mauris hendrerit ante.",
        },
        {
            "title": "Tips For Personal Portfolio",
            "institution": "University of Studies",
            "period": "1997 - 2001",
            "grade": "4.80/5",
            "description": "If you are going to use a passage. Ut tincidunt est ac dolor aliquam sodales. Phasellus sed mauris hendrerit, laoreet sem in, lobortis mauris hendrerit ante.",
        },
    ],
    "experience": [
        {
            "title": "Diploma in Web Development",
            "institution": "BSE In CSE",
            "period": "2004 - 2008",
            "grade": "4.70/5",
            "description": "Contrary to popular belief. Ut tincidunt est ac dolor aliquam sodales. Phasellus sed mauris hendrerit, laoreet sem in, lobortis mauris hendrerit ante.",
        },
        {
            "title": "The Personal Portfolio Mystery",
            "institution": "Job at Rainbow-Themes",
            "period": "2008 - 2016",
            "grade": "4.95/5",
            "description": "Generate Lorem Ipsum which looks. Ut tincidunt est ac dolor aliquam sodales. Phasellus sed mauris hendrerit, laoreet sem in, lobortis mauris hendrerit ante.",
        },
        {
            "title": "Diploma in Computer Science",
            "institution": "Works at Plugin Development",
            "period": "2016 - 2020",
            "grade": "5.00/5",
            "description": "Maecenas finibus nec sem ut imperdiet. Ut tincidunt est ac dolor aliquam sodales. Phasellus sed mauris hendrerit, laoreet sem in, lobortis mauris hendrerit ante.",
        },
    ],
}


@app.route("/deploy", methods=["POST"])
def deploy():
    try:
        # Run the deployment script
        result = subprocess.run(["./deploy.sh"], capture_output=True, text=True)
        if result.returncode != 0:
            return jsonify({"error": result.stderr}), 500
        return (
            jsonify({"message": "Deployment successful", "output": result.stdout}),
            200,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def index():
    return render_template(
        "index.html",
        experiences=experiences,
        education=education,
        portfolio=portfolio,
        resume=resume,
    )


if __name__ == "__main__":
    app.run(debug=True)
