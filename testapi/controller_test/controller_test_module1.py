import unittest

'''

'''

def test_1(self):
    c = 'a'
    encode = 'json'
    charset = 'utf-8'
    callback = ''
    print(self.Controller.hitokoto(c, encode, charset, callback)['id'])
    print(self.Controller.hitokoto(c, encode, charset, callback)['hitokoto'])
    print(self.Controller.hitokoto(c, encode, charset, callback)['type'])
    print(self.Controller.hitokoto(c, encode, charset, callback)['from'])
    print(self.Controller.hitokoto(c, encode, charset, callback)['creator'])
    print(self.Controller.hitokoto(c, encode, charset, callback)['created_at'])
    self.assertEqual(self.Controller.hitokoto(c, encode, charset, callback)['type'], 'a')
