#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'DA SILVA MENDONCA Thomas'
SITENAME = 'portfolio_DaSilvaMendonca'
SITEURL = ''
LOGO = 'teemtho_Crosscode'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = TrueTHEME = 'themes/mon-theme-pelican'

THEME = 'themes/mon-theme-pelican'
CSS_FILE = 'portfolio.css'

MENU = (
	('#apropos', 'À Propos'),
    ('#cursus', 'Cursus'),
    ('#competences','Competences'),
	('#contributions', 'Contributions'),
	('#contact', 'Contact')
)


COMPETENCE1 = (
(('PHP (en travaillant sur des projets professionels en Symfony et Thelia)'),('80%')),

(('Python'), ('70%')),

(('Java et JavaFX'),('70%')),

(('WEB (HTML, CSS, Bootstrap)'),('70%')),

)

COMPETENCE1POURCENT = (
('80%'),
('70%'),
('70%'),
('70%')
)

COMPETENCE2 = (
('Autonome'),
('Travail en équipe'),
('Curieux '),
)

COMPETENCE3 = (
('Niveau d\'Anglais : B2'),
)


# Formulaire de contact
TITRE_CONTACT = 'Contactez moi'
NOM_FORM = 'Formulaire de contact'
CHAMPS_CONTACT = (
	('Nom', 'text', 'nom', 'Entrez votre nom.'),
	('E-mail', 'email', 'email','Saisissez votre adresse e-mail.' ),
	('Message', 'textarea', 'message', 'Saisissez votre message.')
)

OUTPUT_PATH = 'public'




