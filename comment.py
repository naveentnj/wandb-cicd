import os
from ghapi.core import GhApi
owner,repo = os.environ['REPO'].split('/')
api = GhApi(owner=owner, repo=repo)
api.issues.create_comment(os.environ['NUMBER'], "Hi! I'm making a comment with `ghapi` in Actions!")
