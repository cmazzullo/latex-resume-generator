#!/usr/bin/env python

'''Generate a latex resume from a dict of strings containing resume
info (name, work experiences, etc)'''


resume = {
    'first_name': 'Christopher',
    'last_name': 'Mazzullo',
    'phone': '5712634291',
    'email': 'chris.mazzullo@gmail.com',
    'website': 'cmazzullo.github.io',
    'objective': 'to do stuff',
    'education': {
        'school': 'George Mason University',
        'major': 'Physics',
        'minor': 'Computer Science',
        'grad_date': '2015',
        'location': 'Fairfax',
        'degree': 'BS'
    },
    'experience': [
        {'company': 'USNO',
         'dates': ['Sept 2015', 'Present'],
         'location': 'Washington, DC',
         'bullets': ['b1', 'b2', 'b3'],
         'title': 'eop engineer'},
        {'title': 'Python Developer',
         'company': 'USGS',
         'dates': ['Sept 2014', 'May 2015'],
         'location': 'Reston, VA',
         'bullets': ['b1', 'b2', 'b3']}
    ],
    'skills': ['skills1', 'skill2']
}



def latexify_experience(experience):
    string = r'''\section{Experience}'''
    def latexify_job(job):
        string = r'''\cventry{{{dates}}}{{{title}}}{{{company}}}{{{location}}}{{}}{{
        \begin{{itemize}}'''.format(**job)
        for bullet in job['bullets']:
            string += '''\item {}'''.format(bullet)
        string += '''\end{itemize}}'''
        return string
    for job in experience:
        string += latexify_job(job)
    return string


whole_doc = r'''
{header}
{contact}

\begin{{document}}
\makecvtitle

{objective}
{education}
{experience}
{skills}

\end{{document}}
'''

def latexify(d):
    header = r'''\documentclass[11pt,a4paper,sans]{moderncv}
    \moderncvstyle{banking}
    \moderncvcolor{blue}
    \usepackage[scale=0.75]{geometry}'''

    contact = r'''\name{{{first_name}}}{{{last_name}}}
    \phone{{{phone}}}
    \email{{{email}}}
    \social[github]{{{website}}}'''.format(**d)

    objective = r'''\section{{Objective}}
    \cvitem{{}}{{{0}}}'''.format(d['objective'])

    edu = d['education']
    education = '''\section{{Education}}
    \cventry{{{grad_date}}}{{\emph{{{degree}}} {major}, Minor {minor}}}
    {{{school}}}{{{location}}}{{}}{{}}'''.format(**d['education'])
    
    experience = latexify_experience(d['experience'])

    skills = r'\section{Skills}'
    for skill in d['skills']:
        skills += r'\cvlistitem{{{}}}'.format(skill)
    return whole_doc.format(
        header=header,
        contact=contact,
        objective=objective,
        education=education,
        experience=experience,
        skills=skills)

print(latexify(resume))

