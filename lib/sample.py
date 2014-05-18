from meta_logging import log


@log()
class MySimpleClass(object):
    def ok(self):
        """I return ok"""
        return "ok"
    def no(self):
        """this is no"""
        return "no"

that = MySimpleClass()
that.ok()
that.no()
that.no()
that.no()
