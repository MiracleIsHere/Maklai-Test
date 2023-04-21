from typing import List, Optional

from fastapi import Depends, FastAPI
from nltk.tree import Tree
from pydantic import BaseModel

from nltk_utils import paraphrase, tree_to_str

app = FastAPI()


class ParaphraseRequest(BaseModel):
    tree: str
    limit: Optional[int] = 20


class ParaphraseResponse(BaseModel):
    paraphrases: List[dict]


@app.get('/paraphrase')
def get_paraphrase(request: ParaphraseRequest = Depends()) -> ParaphraseResponse:
    tree_str = request.tree
    limit = request.limit

    tree = Tree.fromstring(tree_str)
    paraphrased_trees = paraphrase(tree, limit)
    paraphrases = [{"tree": tree_to_str(tree)} for tree in paraphrased_trees]

    return ParaphraseResponse(paraphrases=paraphrases)
