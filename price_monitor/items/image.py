# -*- coding: utf-8 -*-

from scrapy import Item, Field

class Image(Item):
    # Array indexes. 
    KEY_IS_MAIN = 'is_main'
    KEY_LANGUAGE = 'language'
    KEY_STORE_ID = 'store_id'
    KEY_URL = 'url'

    # Fields.
    is_main = Field()
    language = Field()
    store_id = Field()
    url = Field()

    def get_dictionary(self):
        return dict(self)