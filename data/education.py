#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created By: jalco on 25/08/2020

def get_education_data():
    education = [
        {
            'school': 'University of Huddersfield',
            'level': 'incomplete',
            'grades': [
                    {
                        'qualification': 'Computer Games Programming',
                        'grade': 'incomplete',
                    },
                ],
        },
        {
            'school': "Monks' Dyke Technology College",
            'level': 'GSCE',
            'grades': [
                {'qualification': 'English', 'grade': 'C', },
                {'qualification': 'Math', 'grade': 'B', },
                {'qualification': 'Science', 'grade': 'B', },
                {'qualification': 'German', 'grade': 'C', },
            ],
        }
    ]

    return education


if __name__ == '__main__':
    education = get_education_data()

    for ed in education:
        print(ed['school'])
        print(ed['level'])
        for grade in ed['grades']:
            print(grade['qualification'])
            print(grade['grade'])
