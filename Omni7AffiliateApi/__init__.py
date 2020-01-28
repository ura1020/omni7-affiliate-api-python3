# coding: utf-8
# author: ura1020

import hmac
import hashlib
import base64
import urllib.parse

endpoint = 'https://7af-api.omni7.jp/af_api/affiliate/rest/'

class New:
  '''
  オムニ7│セブンアフィリエイト
  https://7af.omni7.jp/af_static_site/API1.html
  '''

  def __init__(self, api_user_id, secret_key):
    self.api_user_id = api_user_id
    self.secret_key = secret_key

  def make_signature(self, source, key):
    source_encode = urllib.parse.quote(source,safe='')
    return base64.b64encode(hmac.new(key.encode('utf-8'), source_encode.encode('utf-8'), hashlib.sha256).digest()).decode("utf-8")

  def build_url(self, method, api, params):
    kvstr = sorted(["%s=%s" % (k,v) for k,v in params.items()])
    params['Signature'] = self.make_signature("|".join([method] + [api] + kvstr), self.secret_key)
    return api + '?' + urllib.parse.urlencode(params)

  def get_json(self, api_name, params):
    import datetime
    return self.build_url('GET', "%s%s" % (endpoint, api_name), dict({
      'ApiUserId': self.api_user_id,
      'Timestamp': datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
      'ResponseFormat': 'JSON',
    }, **params))

  def get_shopping_category_url(self, params):
    '''
    カテゴリ検索
    https://7af.omni7.jp/af_static_site/API2.html
    '''
    return self.get_json('GetShoppingCategory', params)

  def search_product_url(self, params):
    '''
    商品検索
    https://7af.omni7.jp/af_static_site/API3.html
    '''
    return self.get_json('SearchProduct', params)

  def search_ranking_url(self, params):
    '''
    ランキング検索
    https://7af.omni7.jp/af_static_site/API4.html
    '''
    return self.get_json('SearchRanking', params)

  def search_product_review_url(self, params):
    '''
    商品レビュー検索
    https://7af.omni7.jp/af_static_site/API5.html
    '''
    return self.get_json('SearchProductReview', params)
