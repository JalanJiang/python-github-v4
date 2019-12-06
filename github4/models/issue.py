'''
@Description: Issue 封装
@Version: v1.0
@Author: JalanJiang
@Date: 2019-10-21 11:32:39
@LastEditTime: 2019-10-29 17:59:43
'''
from github4.tools.request import Request

class Issue():
    def __init__(self, request, id, title):
        '''
        @description: 构造函数
        @param request: 请求工具封装
        @param id: Issue ID 
        @return: None
        '''
        self.request = request
        self.id = id
        self.title = title

    def close(self):
        '''
        @description: 关闭 Issue
        @return: None
        '''
        mutation = """
        mutation
        {
            closeIssue(input: {issueId: "%s"}) {
                clientMutationId
            }
        }
        """% (self.id)
        data = self.request.query_request(query=mutation)
        # Todo：请求结果处理
        return data