# # -*- coding:utf8 -*-
# import json


# from app.common.util.httpUtil.responseUtil import writeSuccess2Response

# from app.core.model.baseModel import Result
# from app.web import controllers
# from flask import request

# RequestMapping = '/api/test'


# @controllers.route(RequestMapping + '/test.json', methods=['GET', 'POST'])
# def getTestController():
#     result = Result()
#     if request.method != 'GET':
#         result.setSuccess(False)
#         resp = writeSuccess2Response(result)
#         return resp

#     result.setData("查询成功")
#     result.setSuccess(True)

#     return writeSuccess2Response(result)



# # users = set()
# # @controllers.route(RequestMapping + '/test2.json')
# # def handle_websocket():
# #     wsock = request.environ.get('wsgi.websocket')
# #     users.add(wsock)
# #     if not wsock:
# #         abort(400, 'Expected WebSocket request.')
# #     while True:
# #         try:
# #             message = wsock.receive()
# #         except WebSocketError:
# #             break
# #         print u"现有连接用户：%s" % (len(users))
# #         if message:
# #             for user in users:
# #                 try:
# #                     user.send(message)
# #                 except WebSocketError:
# #                     print u'某用户已断开连接'
# #     # 如果有客户端断开，则删除这个断开的websocket
# #     users.remove(wsock)
