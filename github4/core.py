'''
@Description: 核心类
@Version: v1.0
@Author: JalanJiang
@Date: 2019-10-12 10:37:25
@LastEditTime: 2019-10-29 17:43:24
'''
import json

from github4.models.repo import Repo
from github4.tools.request import Request


class Github:

    BASE_URL = "https://api.github.com/graphql"

    def __init__(self, access_token=None):
        '''
        @description: 构造函数
        @param access_token: Github AccessToken 
        @return: None
        '''
        self.access_token = access_token
        self.request = Request(access_token=self.access_token)
        
    def get_user(self):
        '''
        @description: 获取用户数据
        @return: 字典结构请求结果
        '''
        query = """
        {
            viewer {
                bio
                company
                createdAt
                email
                id
                login
                name
            }
        }
        """
        data = self.request.query_request(query=query)
        return data

    def get_repo(self, repo_name):
        '''
        @description: 根据仓库名称获取仓库
        @param repo_name: 仓库名称
        @return: Repo 对象
        '''
        query = """
        {
            viewer {
                repository(name: "%s") {
                    id
                    name
                    issues(last: 100, states: OPEN) {
                        nodes {
                            id
                            title
                        }
                    }
                }
            }
        }
        """ % (repo_name)
        # Todo: 异常捕获
        data = self.request.query_request(query=query)
        repository = data['data']['viewer']['repository']

        return Repo(
            request=self.request,
            id=repository['id'], 
            name=repository['name'], 
            issues=repository['issues']['nodes']
        )
