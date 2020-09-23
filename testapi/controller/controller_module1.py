from common.common_url import hitokoto_url
from common.request_utils import Utils

class controller_hitokoto():
    util = Utils

    def get_hitokoto(self, c, encode, charset, callback):
        payload = {
                'c': c,
                'encode': encode,
                'charset': charset,
                'callback': callback,
                }
        r = self.util.get(hitokoto_url,params=payload)
        return r.json()

