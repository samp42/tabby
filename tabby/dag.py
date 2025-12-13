from __future__ import annotations

from typing import TypeVar
import numpy as np

T = TypeVar('T')

class DAGNode:
    id = 0 # static
    # data: T
    name: str | None

    def __init__(self, name: str | None = None):
        self.id = DAGNode.id + 1
        DAGNode.id += 1
        self.name = name

class DAG:
    nodes: DAGNode
    adj: np.ndarray
    name: str | None

    def __init__(self, name: str | None = None):
        self.name = name
        self.nodes = []
        self.adj = np.zeros((0, 0))

    def add_node(self, node: DAGNode, parent_ids: list | None = None):
        if any(n.id == node.id for n in self.nodes):
            raise Exception('Node with id already exists')
        elif parent_ids is not None and any(parent_id not in [n.id for n in self.nodes] for parent_id in parent_ids):
            raise Exception('Parent id does not exist')
        else:
            self.nodes.append(node)
            if parent_ids is not None:
                for parent_id in parent_ids:
                    parent_index = next(i for i, n in enumerate(self.nodes) if n.id == parent_id)
                    child_index = len(self.nodes) - 1
                    new_adj = np.zeros((len(self.nodes), len(self.nodes)))
                    new_adj[:self.adj.shape[0], :self.adj.shape[1]] = self.adj
                    self.adj = new_adj
                    self.adj[parent_index][child_index] = 1
            else:
                new_adj = np.zeros((len(self.nodes), len(self.nodes)))
                new_adj[:self.adj.shape[0], :self.adj.shape[1]] = self.adj
                self.adj = new_adj

    def mount_subdag(self, subdag: DAG, parent_ids: list | None = None):
        if parent_ids is not None and any(parent_id not in [n.id for n in self.nodes] for parent_id in parent_ids):
            raise Exception('Parent id does not exist')
        else:
            id_mapping = {}
            for sub_node in subdag.nodes:
                new_node = DAGNode(sub_node.name)
                self.add_node(new_node)
                id_mapping[sub_node.id] = new_node.id
            for i, sub_node in enumerate(subdag.nodes):
                for j, sub_node2 in enumerate(subdag.nodes):
                    if subdag.adj[i][j] == 1:
                        parent_index = next(k for k, n in enumerate(self.nodes) if n.id == id_mapping[sub_node.id])
                        child_index = next(k for k, n in enumerate(self.nodes) if n.id == id_mapping[sub_node2.id])
                        self.adj[parent_index][child_index] = 1
            if parent_ids is not None:
                for parent_id in parent_ids:
                    for sub_root in subdag.get_roots():
                        parent_index = next(i for i, n in enumerate(self.nodes) if n.id == parent_id)
                        child_index = next(i for i, n in enumerate(self.nodes) if n.id == id_mapping[sub_root])
                        self.adj[parent_index][child_index] = 1

    def get_critical_path(self) -> list:
        # Find the longest path in the DAG
        # Return list of node ids
        # Take into account that there can be multiple roots and leaves
        num_nodes = len(self.nodes)
        dist = [-float('inf')] * num_nodes
        for i in range(num_nodes):
            if all(self.adj[j][i] == 0 for j in range(num_nodes)):  # root node
                dist[i] = 0
        for i in range(num_nodes):
            for j in range(num_nodes):
                if self.adj[i][j] == 1:
                    dist[j] = max(dist[j], dist[i] + 1)
        max_dist = max(dist)
        critical_path = []
        for i in range(num_nodes - 1, -1, -1):
            if dist[i] == max_dist:
                critical_path.append(self.nodes[i].id)
                max_dist -= 1
        return critical_path[::-1]

    def get_roots(self):
        roots = []
        for i, node in enumerate(self.nodes):
            if all(self.adj[j][i] == 0 for j in range(len(self.nodes))):
                roots.append(node.id)
        return roots

    # def get_leaves(self):
    #     leaves = []
    #     for i, node in enumerate(self.nodes):
    #         if all(self.adj[i][j] == 0 for j in range(len(self.nodes))):
    #             leave.append(node.id)
    #     return leaves
