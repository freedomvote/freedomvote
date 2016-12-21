from django.conf import settings


# returns the language codes from the django settings. ['de', 'en']
def get_setting_lang_code():
    return [lang[0] for lang in settings.LANGUAGES]


# calls the function with the given attr and languages.
# text_de, text_en
def model_lang_fields(obj, attr, lang):
    return {
        lang_code: model_lang_field(obj, '%s_%s' % (attr, lang_code))
        for lang_code in lang
    }


# return empty string if the return value of getattr is None
def model_lang_field(obj, attr):
    value = getattr(obj, attr)
    return value if value is not None else ''
