'''
@Description: 仓库类
@Version: v1.0
@Author: JalanJiang
@Date: 2019-10-21 16:07:42
@LastEditTime: 2019-10-29 18:14:42
'''
from github4.models.issue import Issue


class Repo():
    def __init__(self, request, id, name, issues=None):
        '''
        @description: 构造函数
        @param request: 请求工具
        @param id: 仓库 ID
        @param name: 仓库名称
        @param issues: Issues 列表 
        @return: 
        '''
        self.id = id
        self.name = name
        self.issues = self.__init_issue(request, issues)
        self.request = request

    def get_issues(self):
        # Todo：返回 Issue 对象
        return self.issues

    def create_issue(self, issue_name, body):
        '''
        @description: 在 Repo 中创建 issue
        @doc: https://developer.github.com/v4/input_object/createissueinput/
        @doc: https://developer.github.com/v4/mutation/createissue/
        @param : 
        @return: 
        '''
        mutation = """
        mutation
        {
            createIssue(input: {
                repositoryId: "%s",
                title: "%s",
                body: "%s"
            }) {
                clientMutationId
            }
        }
        """% (self.id, issue_name, body)
        data = self.request.query_request(query=mutation)
        return data

    @staticmethod
    def __init_issue(request, issues):
        issue_list = []
        for issue in issues:
            issue_list.append(Issue(request=request, id=issue['id'],title=issue['title'],))
        return issue_list