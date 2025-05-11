# EdgeRank Simulator

A simulation of the **EdgeRank algorithm**, originally developed by Facebook to determine which posts should appear in a user's news feed. This project provides a simplified yet functional version of the algorithm, allowing interaction analysis, content ranking, and post search functionalities.

## Features

### ✅ EdgeRank Algorithm  
Implements a simplified EdgeRank algorithm that considers:
- User affinity based on previous interactions
- Popularity of the post
- Time-decay factor for older posts

### ✅ Interaction Types  
- Reactions: `likes`, `loves`, `wows`, `hahas`, `sads`, `angrys`, `special`
- Comments
- Shares

### ✅ User Affinity Calculation  
Affinity is based on:
- Type of interaction with the post author (reactions, comments, shares, friendship)
- Relative weight of each action (e.g., sharing is weighted more than liking)

### ✅ Popularity Estimation  
Based on the total number of interactions (reactions, comments, shares) a post receives.

### ✅ Time Decay Factor  
More recent posts are prioritized using a time-based decay formula.

### ✅ Search Engine with Ranking  
- Keyword-based search of post content
- Ranking influenced by keyword frequency and EdgeRank score
- Supports multi-word queries
- Phrase search using quotes (e.g., `"happy birthday"`)
- Autocomplete suggestions using wildcard (e.g., `dan*` → `Danette`, `Daniel`, etc.)

### ✅ Graph-Based User Network  
User relationships are modeled as a graph to analyze direct connections.

### ✅ Trie Structure for Efficient Word Search  
Speeds up word lookup and autocomplete suggestions.

### ✅ Serialization Support  
Speeds up application startup by saving and loading preprocessed structures.

## Console Menu

Includes a console-based menu for:
- User login
- Browsing personalized post feed
- Performing searches

**Note:** Search types (keyword, phrase, autocomplete) are inferred based on input formatting:
- Quotes → Phrase search
- Asterisk (`*`) → Autocomplete
- Words separated by space → Multi-word search

## Data Files

Project uses CSV data files provided for testing:

- `statuses.csv`: Posts with metadata and reaction counts  
- `comments.csv`: Comments on posts  
- `friends.csv`: Friendship relations among users  
- `reactions.csv`: User reactions to posts  
- `shares.csv`: User shares of posts  

## Technologies Used

- Python 3 (or another appropriate language)
- CSV file parsing
- Trie data structure
- Graphs (adjacency list for friends)
- Serialization (using `pickle`)

## Getting Started

1. Clone the repository
2. Run the main application script
3. Follow the on-screen menu to log in and interact with the system

