# coding=utf-8

class Result:
    resultMessage = ""
    resultCode = ""
    success = False
    data = {}

    def setData(self, data):
        self.data = data

    def setSuccess(self, status):
        self.success = status
