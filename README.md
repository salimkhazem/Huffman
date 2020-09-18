# Huffman

A Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression.
The Huffman Coding is a lossless data compression algorithm, developed by David Huffman in the early of 50s while he was a PhD student at MIT. The algorithm is based on a binary-tree frequency-sorting method that allow encode any message sequence into shorter encoded messages and a method to reassemble into the original message without losing any data.


<H2>The Basics of algorithm </H2> 

The algorithm is based on the frequency of occurrence of the data item(byte). The most frequent data items will represented and encoded with a lower number of bits.
The main idea of the algorithm is create a binary tree, called Huffman tree, 
based on the bytes frequency on the data, where the leafs are the bytes symbols, and the path from the root to a leaf determines the new representation of that leaf byte.


<H2>Building the Tree </H2> 


Each node of the tree are represented with a byte symbol and the frequency of that byte on the data. 
The creation of the Huffman tree have the following steps:
<u> 
<li> Scan the data and calculate the frequency of occurrence of each byte </li> 
<li> Insert those nodes into a reverse priority queue based on the frequencies(a lowest frequency is given highest priority)</li> 
<li> Start a loop until the queue is empty </li> 
<li> Remove two nodes from the queue and combine them into a internal node with the frequency equal to the sum of the two nodes frequencies </li> 
<li> Insert the two nodes removed from the queue as children of the created internal node </li> 
<li> Insert the created internal node into the queue </li> 
<li> The last node remaining on the queue is the root of the tree </li> 
  
  </u> 
  
  
  
  
  Using the text ABCBAACD as example and applying those steps, we have the following tree: 
  
  
  ![Capture d’écran 2020-09-19 à 01 05 03](https://user-images.githubusercontent.com/26838474/93652114-2a0ce700-fa14-11ea-9b66-283a74b5deee.png)
  
  
  
  
  So the new representation of the bytes on the text are:

<u> 
<li> A: 0 </li>
<li>B: 10 </li>
<li>C: 111</li>
<li>D: 110</li>
  </u>



<H2> References </H2>

<u> 
  <li> https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1126/handouts/220%20Huffman%20Encoding.pdf </li> 
  
  <li> https://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/ </li> 
  
  <li> https://kamilmysliwiec.com/implementation-of-huffman-coding-algorithm-with-binary-trees </li> 
  
  
  
  </u>
  
  
  
  
  
  
  
  
  <H4> This Repository is the Implementation of the algorithm using Python  </H4> 

  
