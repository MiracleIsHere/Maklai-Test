from copy import deepcopy
from itertools import permutations
from typing import List

from nltk.tree import Tree


def paraphrase(tree: Tree, limit: int = 20) -> List[Tree]:
    """
    Generates paraphrases of the input syntactic tree by permuting the children of
    all NP nodes that have either ('NP' and ',') or ('NP' and 'CC') as direct children.

    Args:
    - tree: A Tree object representing the input syntactic tree.
    - limit: An integer indicating the maximum number of paraphrases to generate.

    Returns:
    - A list of generated paraphrases, each represented as a Tree object.
    """

    # Extract all NP nodes from the given tree
    np_nodes = []
    for pos in tree.treepositions():
        if isinstance(tree[pos], Tree) and tree[pos].label() == "NP":
            np_nodes.append((pos, tree[pos]))

    # Filter out NP nodes that have 'NP' and ',' or 'NP' and 'CC' as their direct children
    np_nodes_filtered = []
    for pos, node in np_nodes:
        direct_children = [node[i].label() for i in range(
            len(node)) if isinstance(node[i], Tree)]
        if ('NP' and ',' in direct_children) or ('NP' and 'CC' in direct_children):
            np_nodes_filtered.append((pos, node))

    # Generate all possible permutations of the children of the filtered NP nodes
    nodes_permutations = []
    for parent_pos, parent_node in np_nodes_filtered:
        children_to_permute, children_indexes_constant = [], []
        for i in range(len(parent_node)):
            # ',' and 'CC' do not participate in permutation
            if isinstance(parent_node[i], Tree) and parent_node[i].label() in [',', 'CC']:
                children_indexes_constant.append((i, parent_node[i]))
            else:
                children_to_permute.append(parent_node[i])

        source_permutations = permutations(children_to_permute)

        # Insert ',' and 'CC' in permutations
        restored_permutations = []
        for permutation in source_permutations:
            cur_permutation = list(permutation)
            for i, val in children_indexes_constant:
                cur_permutation.insert(i, val)
            restored_permutations.append(cur_permutation)
        # Skip the 0-indexed permutation since it is identical to the input
        nodes_permutations.append((parent_pos, restored_permutations[1:]))

    # Generate paraphrased trees by replacing the children of the filtered NP nodes with their permutations
    paraphrased_trees = [deepcopy(tree)]
    for parent_pos, children_permutations in nodes_permutations:
        cur_paraphrased_trees = []
        for paraphrased_tree in paraphrased_trees:
            for children_permutation in children_permutations:
                new_tree = deepcopy(paraphrased_tree)
                parent_node = new_tree[parent_pos]
                for i in range(len(children_permutation)):
                    parent_node[i] = children_permutation[i]
                cur_paraphrased_trees.append(new_tree)

                # Return paraphrased trees if limit is riched
                if len(paraphrased_trees) + len(cur_paraphrased_trees) == limit+1:
                    paraphrased_trees.extend(cur_paraphrased_trees)
                    # Skip the input tree
                    return paraphrased_trees[1:]

        paraphrased_trees.extend(cur_paraphrased_trees)

    # Skip the input tree
    return paraphrased_trees[1:]


def tree_to_str(tree):
    """
    String representation of Tree without offsets and indents.
    """

    if isinstance(tree, str):
        return tree
    else:
        return "(" + tree.label() + " " + " ".join([tree_to_str(child) for child in tree]) + ")"
