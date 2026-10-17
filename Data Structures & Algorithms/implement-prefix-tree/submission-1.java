class PrefixTree {
    class Node {
        Node[] children;
        boolean isWord; // Marks the end of an inserted word
        
        Node() {
            this.children = new Node[26];
            this.isWord = false;
        }
    }

    Node root; 

    public PrefixTree() {
        this.root = new Node();
    }

    public void insert(String word) {
        Node curr = root; 
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            // If the path doesn't exist, create a new node
            if (curr.children[index] == null) {
                curr.children[index] = new Node();
            }
            // Move down the tree
            curr = curr.children[index];
        }
        // Mark the final node as the end of a complete word
        curr.isWord = true; 
    }

    public boolean search(String word) {
        Node curr = root; 
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            // If the path breaks early, the word doesn't exist
            if (curr.children[index] == null) {
                return false;
            }
            curr = curr.children[index];
        }
        // The path exists, but is it a fully inserted word?
        return curr.isWord; 
    }

    public boolean startsWith(String prefix) {
        Node curr = root; 
        for (char c : prefix.toCharArray()) {
            int index = c - 'a';
            // If the prefix path breaks early, it's not in the tree
            if (curr.children[index] == null) {
                return false;
            }
            curr = curr.children[index];
        }
        // If we successfully navigated the whole prefix, it exists
        return true; 
    }
}