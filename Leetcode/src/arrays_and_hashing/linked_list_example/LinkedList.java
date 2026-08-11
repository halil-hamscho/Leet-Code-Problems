package arrays_and_hashing.linked_list_example;

class Node {
    int data;
    Node next; // Reference to the next node

    // Constructor to a new node
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}
// LinkedList class
public class LinkedList {
    private Node head; // head of the linked list

    public LinkedList() {
        this.head = null;
    }

    // Method to add at the end of the list
    public void add(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            // Starting at the head
            Node current = head;
            // Traverse to the end
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode; // append at the end
        }
    }
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public void remove(int data) {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }
        // If the head node needs to be removed
        if (head.data == data) {
            head = head.next;
            return;
        }
        // Traverse the list to find the node (always start at the head)
        Node current = head;
        while (current.next != null && current.next.data != data) {
            current = current.next;
        }
        if (current.next != null) { // Found the node
            current.next = current.next.next;
        } else {
            System.out.println("Node with value " + data + " was not found.");
        }

    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.add(10);
        list.add(20);
        list.add(30);

        list.printList();

        list.remove(20);
        list.printList();
    }
}

