import random
from networkx.algorithms import community
from networkx.algorithms.community.quality import modularity

# Sample the graph for performance
sampled_nodes = random.sample(list(G.nodes), min(500, len(G.nodes)))  # Limit to 500 nodes or fewer
G_sampled = G.subgraph(sampled_nodes)

# Community Detection Using Greedy Modularity
def detect_communities_and_calculate_modularity(graph):
    """
    Detects communities in the graph using the Louvain method and calculates modularity.
    """
    # Detect communities using the Greedy Modularity algorithm
    communities = community.greedy_modularity_communities(graph)
    
    # Assign each node to a community
    community_map = {}
    for idx, comm in enumerate(communities):
        for node in comm:
            community_map[node] = idx

    # Add the community as a node attribute for visualization
    nx.set_node_attributes(graph, community_map, "community")

    # Calculate modularity score
    modularity_score = modularity(graph, [set(comm) for comm in communities])

    # Visualize the graph with communities
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph)  # Position nodes for visualization
    for comm_idx, comm in enumerate(communities):
        nx.draw_networkx_nodes(graph, pos, nodelist=list(comm), label=f"Community {comm_idx}")
    
    nx.draw_networkx_edges(graph, pos, alpha=0.5)
    nx.draw_networkx_labels(graph, pos, font_size=8)
    plt.title(f"Community Detection in the Network (Modularity Score: {modularity_score:.2f})")
    # plt.legend()
    plt.show()

    return modularity_score

# Perform community detection and calculate modularity
modularity_score = detect_communities_and_calculate_modularity(G_sampled)
print(f"Modularity Score: {modularity_score:.2f}")