import unittest

from nltk.tree import Tree

from nltk_utils import paraphrase

TREE_STR = '''
(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP 
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ 
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS 
restaurants) ) ) ) ) ) ) )
'''


class TestNLTKUtils(unittest.TestCase):

    def test_paraphrase_np(self):
        tree = Tree.fromstring(TREE_STR)
        paraphrased_trees = paraphrase(tree)
        self.assertEqual(len(paraphrased_trees), 11)

    def test_paraphrase_np_limited(self):
        tree = Tree.fromstring(TREE_STR)
        paraphrased_trees = paraphrase(tree, limit=5)
        self.assertEqual(len(paraphrased_trees), 5)

    def test_paraphrase_no_np(self):
        tree = Tree.fromstring("(S (VP (VBZ is) (NP (DT a) (NN sentence))))")
        paraphrased_trees = paraphrase(tree, limit=5)
        self.assertEqual(len(paraphrased_trees), 0)


if __name__ == '__main__':
    unittest.main()
