import graphene

class Post(graphene.ObjectType):
    title = graphene.String()
    content = graphene.String()

class Query(graphene.ObjectType):
    post = graphene.Field(Post)

    def resolve_post(self, info):
        return {'title': 'Sample Title', 'content': 'Sample Content'}

schema = graphene.Schema(query=Query)
