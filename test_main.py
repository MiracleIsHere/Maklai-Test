import unittest

from fastapi.testclient import TestClient

from main import app


class TestMain(unittest.TestCase):
    def test_valid_input(self):
        tree_str = '(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) )'
        limit = 1

        response = client.get(f'/paraphrase?tree={tree_str}&limit={limit}')

        assert response.status_code == 200
        assert len(response.json()["paraphrases"]) == limit
        assert all([isinstance(p["tree"], str)
                    for p in response.json()["paraphrases"]])


if __name__ == '__main__':
    client = TestClient(app)
    unittest.main()
