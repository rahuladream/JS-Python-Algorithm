// User defined class node
class Node {
    constructor(ele)
    {
        this.ele = ele
        this.next = null
    }
}

// Linkedlist class
class Linkedlist {
    constructor(){
        this.head = null;
        this.size = 0;
    }

    // Add an element at the end

    add(ele){
        var node = new Node(ele)
        var current;

        if (this.head == null) 
        {
            this.head = node;
        }
        else{
            current = this.head;

            while(current.next){
                current = current.next;
            }
            current.next = node;
        }
        this.size++;
    }

    size_of_list(){
        console.log(this.size)
    }

    printList(){
        var curr = this.head;
        var str = "";
        while(curr) {
            str += curr.ele + " ";
            curr = curr.next;
        }
        console.log(str);
    }

    removeElement(ele){
        var current = this.head
        var prev = null;

        while(current != null){
            if(current.ele === ele) {
                if(prev === null) {
                    this.head = current.next;
                }
                else{
                    prev.next = current.next;
                }
                this.size--;
                return current.ele
            }
        }
        return -1
    }
}


var ll = new Linkedlist()
// adding element to the list 
ll.add(10); 

ll.size_of_list()

// adding more elements to the list 
ll.add(20); 
ll.add(30); 
ll.add(40); 
ll.add(50); 
  
// returns 10 20 30 40 50 
ll.printList(); 
  
ll.size_of_list()
