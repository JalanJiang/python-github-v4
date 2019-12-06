## Python Github-v4

A Python library to access the [Github API v4](https://developer.github.com/v4/)。

### About GraphQL

#### Queries

Queries are structured like this:

```json
query {
  JSON objects to return
}
```

#### Mutation

```json
mutation {
  mutationName(input: {MutationNameInput!}) {
    MutationNamePayload
}
```

- [Example Mutaion](https://developer.github.com/v4/guides/forming-calls/#example-mutation)

### Example

```python
from github4.core import Github

g = Github("")
g.get_user()
```

### Reference

- [通过 Github V4 API 来了解 GraphQL | 始于珞尘](https://juejin.im/entry/5b04fb1af265da0ba2675892)
- [GraphQL 实战：Github V4 API使用](https://www.jianshu.com/p/af7ac20f2c64)
- [How to consume the Github GraphQL API using Python?](https://stackoverflow.com/questions/45957784/how-to-consume-the-github-graphql-api-using-python)