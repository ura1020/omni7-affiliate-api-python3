# coding: utf-8
# author: ura1020

import Omni7AffiliateApi

api_user_id = 'your api_user_id'
secret_key = 'your secret_key'

api = Omni7AffiliateApi.New(api_user_id, secret_key)

# カテゴリ検索
print(api.get_shopping_category_url({}))
print(api.get_shopping_category_url({'CategoryCode':'401522'}))

# 商品検索
print(api.search_product_url({'KeywordIn': 'ラーメン'}))
print(api.search_product_url({'KeywordIn': 'つけ麺', 'StartIndex': 21, 'ResultAmount': 20}))

# ランキング検索
print(api.search_ranking_url({'CategoryCode':'401522'}))
print(api.search_ranking_url({'CategoryCode':'401522','TermCond':'last1w'}))

# 商品レビュー検索
print(api.search_product_review_url({'ProductCode':'1107064565'}))
print(api.search_product_review_url({'ProductStandardCode':'512-37-7','StartIndex':11,'ResultAmount':10}))
