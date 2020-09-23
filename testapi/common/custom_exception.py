class DatabaseError(Exception):
    def __init__(self, err='数据库连接异常'):
        Exception.__init__(self, err)


class ReadConfigError(Exception):
    def __init__(self, err='Config读取初始化失败'):
        Exception.__init__(self, err)


class MailInitializationError(Exception):
    def __init__(self, err='邮件初始化'):
        Exception.__init__(self, err)


class ReadYamlError(Exception):
    def __init__(self, err='Yaml读取初始化失败'):
        Exception.__init__(self, err)


class AssertionError(Exception):
    def __init__(self, err='断言失败'):
        Exception.__init__(self, err)


class ReadExcelError(Exception):
    def __init__(self, err='读取Excel失败'):
        Exception.__init__(self, err)


class CloseFileError(Exception):
    def __init__(self, err='关闭文件时发生错误'):
        Exception.__init__(self, err)


class LogConfigError(Exception):
    def __init__(self, err='日志配置初始化错误'):
        Exception.__init__(self, err)


class RequestError(Exception):
    def __init__(self, err='请求失败'):
        Exception.__init__(self, err)


class WriteResultError(Exception):
    def __init__(self, err='写入测试结果失败'):
        Exception.__init__(self, err)


class SaveReusltError(Exception):
    def __init__(self, err='保存测试结果失败'):
        Exception.__init__(self, err)

