import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import streamlit as st
import numpy as np
import tabby as tab

def visualize_dag(dag: DAG):
    st.title("DAG Visualization")

    if dag.name:
        st.header(f"DAG: {dag.name}")

    node_ids = [node.id for node in dag.nodes]
    node_labels = {node.id: f"Node {node.id}" for node in dag.nodes}

    st.subheader("Nodes")
    for node in dag.nodes:
        st.write(f"ID: {node.id}, Label: {node_labels[node.id]}")

    st.subheader("Adjacency Matrix")
    st.write(dag.adj)

    st.subheader("Graph Representation")
    for i, parent_node in enumerate(dag.nodes):
        children = [dag.nodes[j] for j in range(len(dag.nodes)) if dag.adj[i][j] == 1]
        if children:
            child_labels = ', '.join([node_labels[child.id] for child in children])
            st.write(f"{node_labels[parent_node.id]} -> {child_labels}")
        else:
            st.write(f"{node_labels[parent_node.id]} -> No children")

if __name__ == "__main__":
    # Example DAG creation
    dag = tab.DAG(name="Example DAG")

    node1 = tab.DAGNode("A")
    dag.add_node(node1)

    node2 = tab.DAGNode("B")
    dag.add_node(node2, [node1.id])

    node3 = tab.DAGNode("C")
    dag.add_node(node3, [node1.id])

    node4 = tab.DAGNode("D")
    dag.add_node(node4, [node2.id, node3.id])

    visualize_dag(dag)
