import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import tabby as tab

if __name__ == "__main__":
    dag = tab.dag.DAG()

    node1 = tab.dag.DAGNode("A")
    dag.add_node(node1)

    node2 = tab.dag.DAGNode("B")
    dag.add_node(node2, [node1.id])

    node3 = tab.dag.DAGNode("C")
    dag.add_node(node3, [node1.id])

    node4 = tab.dag.DAGNode("D")
    dag.add_node(node4, [node2.id, node3.id])

    # pyrefly: ignore [missing-attribute]
    dag.visualize()
