# import sys
# import pathlib

# ROOT = pathlib.Path(__file__).resolve().parents[1]
# sys.path.insert(0, str(ROOT))

import pytest
import numpy as np
import tabby as tab

# from .. import tabby as tab

# @pytest.mark.parametrize("a,b,expected", [
#     (2, 3, 5),
#     (0, 0, 0),
#     (5, 0, 5),
#     (-2, -3, -5),
#     (-2, 3, 1),
#     (10**18, 10**18, 2 * 10**18),
# ])
# def test_add_integers_and_large(a, b, expected):
#     assert add(a, b) == expected

def test_dag_initialization():
    dag = tab.DAG()
    assert dag is not None
    assert len(dag.nodes) == 0
    assert dag.adj.shape == (0, 0)

def test_add_node_no_parent():
    dag = tab.DAG()
    node = tab.DAGNode("A")
    dag.add_node(node)
    assert len(dag.nodes) == 1
    assert dag.nodes[0].name == "A"
    assert dag.adj.shape == (1, 1)
    # assert dag.adj == np.ndarray([[0]])

def test_add_node_parent():
    dag = tab.DAG()
    node1 = tab.DAGNode("A")
    dag.add_node(node1)
    assert len(dag.nodes) == 1
    assert dag.nodes[0].name == "A"
    assert dag.adj.shape == (1, 1)
    # assert dag.adj == np.ndarray([[0]])

    node2 = tab.DAGNode("B")
    dag.add_node(node2, [node1.id])
    assert len(dag.nodes) == 2
    assert dag.nodes[1].name == "B"
    assert dag.adj.shape == (2, 2)
    # assert dag.adj == np.ndarray([[0, 1],
    #                              [0, 0]])


if __name__ == "__main__":
    pytest.main()
