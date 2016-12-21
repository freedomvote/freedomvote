from django.conf import settings


def get_setting_languages():
    """Returns a list of 2-letter language codes."""
    return [lang[0] for lang in settings.LANGUAGES]


def get_model_translations(object, attribute):
    """Calls the appropriate methode on the object from the given
    attribute and language code.
    e.g. object.attribute_language -> QuestionModel.text_de
    Returns a dict with the language code as key and the translation as
    value
    """
    languages = get_setting_languages()
    return {
        language: getattr(object, '%s_%s' % (attribute, language)) or ''
        for language in languages
    }
