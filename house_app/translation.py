from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Property)
class HouseTranslationOptions(TranslationOptions):
    fields = ('title', 'description','address','region','city',)
