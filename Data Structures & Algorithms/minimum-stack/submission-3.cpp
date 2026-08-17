class MinStack {
public:

    vector<int> min_values;
    vector<int> min_stack;
    MinStack() {}
    
    void push(int val) {
        if (min_values.empty() && min_stack.empty()) {
            min_values.push_back(val);
            min_stack.push_back(val);
        } else {
            if (val <= min_values.back()) {
                min_values.push_back(val);
            }

            min_stack.push_back(val);
        }
    }
    
    void pop() {
        int popped = min_stack[min_stack.size() - 1];
        cout << popped;
        cout << min_values.back();
        min_stack.pop_back();

        if (popped == min_values.back()) {
            min_values.pop_back();
        }
    }
    
    int top() {
        return min_stack.back();
    }
    
    int getMin() {
        return min_values.back();
    }
};
