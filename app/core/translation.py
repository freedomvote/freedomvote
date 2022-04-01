from modeltranslation.translator import translator, TranslationOptions
from core import models


class StateTranslationOptions(TranslationOptions):
    fields = ("name",)


class PartyTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "shortname",
    )


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


class QuestionTranslationOptions(TranslationOptions):
    fields = (
        "text",
        "description",
    )


translator.register(models.State, StateTranslationOptions)
translator.register(models.Party, PartyTranslationOptions)
translator.register(models.Category, CategoryTranslationOptions)
translator.register(models.Question, QuestionTranslationOptions)
