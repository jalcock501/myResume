#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created By: jalco on 25/08/2020
from flask import Blueprint
from infrastructure.view_modifiers import response
from data.about import get_about_data
from data.experience import get_experience_data
from data.education import get_education_data
from data.skills import get_skills_data
from data.interests import get_interest_data

blueprint = Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='/home/index.html')
def index():
    about = get_about_data()
    experience = get_experience_data()
    education = get_education_data()
    skills, projects = get_skills_data()
    interests = get_interest_data()

    return {
        'about': about,
        'experience': experience,
        'education': education,
        'skills': skills,
        'projects': projects,
        'interests': interests,
    }
