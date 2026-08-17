class Node {
public:
    int val;
    Node* next;
    Node(int val) : val(val), next(nullptr) {}  // Removed extra semicolon
};

class LinkedList {
public:
    Node* head;
    Node* tail;
    
    LinkedList() {
        // Better approach: start with empty list
        head = nullptr;
        tail = nullptr;
    }

    int get(int index) {
        int i = 0;
        Node* current = head;  // Fixed: = not ->, start at head
        while (current) {
            if (index == i) {
                return current->val;  // Use -> for pointer
            }
            i++;
            current = current->next;  // Fixed: = not ->
        }
        return -1;
    }

    void insertHead(int val) {
        Node* newNode = new Node(val);
        newNode->next = head;  // New node points to old head
        head = newNode;        // Update head to new node
        
        if (tail == nullptr) {  // If list was empty
            tail = head;        // Tail is also the new node
        }
    }
    
    void insertTail(int val) {
        Node* newNode = new Node(val);
        
        if (tail == nullptr) {  // Empty list
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;  // Current tail points to new node
            tail = newNode;        // Update tail to new node
        }
    }

    bool remove(int index) {
        if (head == nullptr) return false;  // Empty list
        
        // Special case: removing head
        if (index == 0) {
            Node* toDelete = head;
            head = head->next;
            if (head == nullptr) {  // List became empty
                tail = nullptr;
            }
            delete toDelete;
            return true;
        }
        
        // Find node at index-1
        Node* prev = head;
        for (int i = 0; i < index - 1 && prev->next; i++) {
            prev = prev->next;
        }
        
        // Check if index is valid
        if (prev->next == nullptr) {
            return false;  // Index out of bounds
        }
        
        // Remove the node
        Node* toDelete = prev->next;
        prev->next = toDelete->next;
        
        // Update tail if we removed the last node
        if (toDelete == tail) {
            tail = prev;
        }
        
        delete toDelete;
        return true;
    }

    vector<int> getValues() {
        vector<int> values;
        Node* current = head;
        
        while (current) {
            values.push_back(current->val);  // Use -> for pointer
            current = current->next;
        }
        
        return values;  // Don't forget to return!
    }
};