import xmlrpc.client

class NaverBlog(object):
    def __init__(self, user_id, api_key):
        self.__server = None
        self.__api_url = 'https://api.blog.naver.com/xmlrpc'
        self.__user_id = user_id
        self.__api_key = api_key
        self.__categories = []

        try:
            self.__set_categories()
        except Exception as e:
            raise e

    def __client(self):
        if self.__server is None:
            self.__server = xmlrpc.client.ServerProxy(self.__api_url)

        return self.__server

    def __set_categories(self):
        categories = self.__client().metaWeblog.getCategories(self.__user_id,
                                                              self.__user_id,
                                                              self.__api_key)

        for category in categories:
            self.__categories.append(category['title'])

    def post(self, title, description, category, publish=True):
        struct = {}
        struct['title'] = title
        struct['description'] = description
        if category in self.__categories:
            struct['categories'] = [category]
        try:
            return self.__client().metaWeblog.newPost(self.__user_id,
                                                      self.__user_id,
                                                      self.__api_key,
                                                      struct,
                                                      publish)
        except Exception as e:
            raise e



def main():
    naver_id = 'darkq4'
    api_key = '2f4184fc7fda8110bea51f0f48c76690'
    naver = NaverBlog(naver_id, api_key)

    title = "news trend 01"
    description = "<h1>news trend test</h1>"
    category = "NewsTrend"

    naver.post(title, description, category)
    
if __name__ == '__main__':
    main()
