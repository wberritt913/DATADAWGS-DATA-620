# Intro:

Using Wikipedia data, we can look at the linked pages within each specific Wikipedia page. We can consider the articles to be nodes and links between articles to be edges. This way, we can analyze the connection between different articles and find which articles are central to specific categories.

# Data Collection:

Using Wiki API, we can acquire articles and their respective categories, links, and metadata. We could graph the relationship where we have edges between articles, or nodes, depending on links representation within each article. If baseball page has a link to tennis page, we would create an edge between the two.

# Ingishts:

From there, we could calculate the different centrality measurements of each article node. This would give us a sense of what articles are most relevant. If one category like politics, has a relatively high centrality, it may indicate a stronger interconnectedness.