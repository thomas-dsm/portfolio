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
(('WEB (HTML, CSS, Bootstrap)'),('70%')),
(('Java et JavaFX'),('70%')),
(('Python (avec Tkinter)'), ('60%')),
)

COMPETENCE2 = (
(('L\'Autonomie'),('J\'ai travaillé en autonomie sur le projets SAP où on me demandé d\'integrer des nouvelles technologies dans mon projets comme SASS')),
(('Le Travail en équipe'),(' Dans le cadre de ma formation en BTS, j\'ai été amené à gerer une équipe pour le developpement d\'une application web sous symfony et une autre en JavaFX')),
(('La Curiosité'),('je m\'interresse aux nouvelles technologies comme aux I.A. (l\'image de profil a été gener par Midjourney)')),
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




