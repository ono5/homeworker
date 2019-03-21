# Translating Python Code
To translate literals in our Python code, we should do the bellow.

1. Include "django.utils.translation"  
2. Using the "gettext" function  

[Ref](https://docs.djangoproject.com/en/2.0/topics/i18n/translation/)

# Standard translations

```bash
from django.utils.translation import gettext as _
output = _('Text to be translated.)
```

# Lazy translations
Django includes lazy versions for all of its translation functions, which have the suffix "_lazy()".

When using the lazy functions, strings are translated when the value is accessed,
rather than when the function is called.

**Point** :

Using gettext_lazy() instead of gettext(), strings are translated when the value is accessed 
rather than when the function is called.

# Translations includeing variables

```bash
from django.utils.translation import gettext as _
month = _('April')
day = '14'
output = _('Today is %(month)s %(day)s') % {'month': month,
                                             'day': day}
```

# Plural forms in translations
For plural forms, you can use ngettext() and ngettext_lazy().

```bash
output = ngettext('there is %(count)d product',
                  'there are %(count)d products',
                  count) % {'count': count}
```

# Translating our own code

We must do the following.

## Edit settings.py file  

```bash
from django.utils.translation import gettext_lazy as _

MIDDLEWARE = [
    # After settings SeesionMiddleware 
    'django.middleware.locale.LocaleMiddleware',
]

LANGAGES = (
    ('en', _('ENGLISH')),
    ('ja', _('JAPANESE')),
)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale/'),
]
```

## Make File
Create the following directory structure inside the main project directory, next to the manage.py file.

```bash
locale/
    en/
    ja/
```

## Do command on shell

```bash
django-admin makemessages --all


# Outputting following sting if the command is success.
processing locale jp
processing locale en
```

# Edit po file

```bash
msgid "JAPANESE"
msgstr "japanese"
```

# Do command on shell again

Confirm mo file to create.

```bash
django-admin compilemessages

processing file django.po in /Users/hono/Desktop/platform/src/locale/en/LC_MESSAGES
processing file django.po in /Users/hono/Desktop/platform/src/locale/jp/LC_MESSAGES
```

# Edit HTML File using Translating templates

Django offers the {% trans %} and {% blocktrans %} template tags to translate strings in templates.

In order to use the translation templates tags, you have to load {% load i18n %} at the top of your template to load them.

