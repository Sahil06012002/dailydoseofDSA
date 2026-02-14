// /*
// class Node{
// int data;
// Node left;
// Node right;
// Node(int data){
// this.data = data;
// left=null;
// right=null;
// }
// }
// */

// class Solution {
// // Function to return a list of nodes visible from the top view
// // from left to right in Binary Tree.
// TreeMap<Integer , Integer > map = new TreeMap<>();

// class NodeInfo {
// int col;
// Node node;
// public NodeInfo(int col , Node node) {
// this.col = col;
// this.node = node;
// }
// }

// static void bfs(Node node, int col){
// Queue<NodeInfo node> q = new LinkedList<>();
// q.add(new NodeInfo(col, node));

// while(!q.isEmpty()){
// int qLen = q.size();
// for(int i=0; i<qLen ; i++){

// NodeInfo nodeInfo = q.poll();
// if(!map.containsKey(nodeInfo.col)){
// map.put(col , nodeInfo.node.val);
// }
// if (nodeInfo.node.left) q.add(new NodeInfo(col-1, node.left));
// if (nodeInfo.node.right) q.add(new NodeInfo(col+1, node.right));
// }

// }

// }

// static ArrayList<Integer> topView(Node root) {
// // code here
// List<Integer> result = new ArrayList<>();
// bfs(root,0);
// for(int val : map.values()){
// result.add(val);
// }

// return result;
// }
// }