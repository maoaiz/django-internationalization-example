django-internationalization-example
===================================

Django internationalization example

###How to use

1) Configure the DATABASES var in your settings.py (i18n requiere a session)

2) Sync de DATABASE `$ python manage.py syncdb`

3) You need to preparate the translations. Use the `makemessages` command:

	/my_app$ django-admin.py makemessages -l es
	/my_app$ django-admin.py makemessages -l fr

why on `/my_app$`?
because the `locale` directory should be into every django app. You need type the  `makemessages` command on every django app that you have localization and internationalization

4) Translate your messages on the django.po files.

Example file: `/my_app/locale/es/LC_MESSAGES/django.po`

before:

	#: templates/base.html:5
	msgid "Hello, this is built with Django Internationalization"
	msgstr ""

after:

	#: templates/base.html:5
	msgid "Hello, this is built with Django Internationalization"
	msgstr "Hola, esto está construido con la Internacionalización de Django"

5) If you have all your translations on django.po files, the next step is to compile the messages:

`/my_app$ django-admin.py compilemessages`

You should see the message: `processing file django.po in /path_to_LC_MESSAGES...`

You are ready! run the server and change to your languages!

(see a demo live)[http://django-internationalization.daiech.com/]

###How it works?
Django internationalitation use L10n (localization) and i18n (internationalization), [see the docs](https://docs.djangoproject.com/en/1.5/topics/i18n/)

