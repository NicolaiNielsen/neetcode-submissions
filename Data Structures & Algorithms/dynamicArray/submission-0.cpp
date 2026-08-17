class DynamicArray {
public:
    int capacity;
    int *array; // saying this will hold an initial memory adress
    int size;

    DynamicArray(int capacity) {
        this->capacity = capacity;
        this->size = 0;
        array = new int[capacity];
        cout << "initial capacity: capcity" << capacity;
    }

    int get(int i) {
        return array[i];
    }

    void set(int i, int n) {
        array[i] = n;
    }

    void pushback(int n) {
        size++;
        if (size > capacity)
        {
            resize();
        }
        array[size - 1] = n;
    }

    int popback() {
        size--;
        int result = array[size];
        array[size] = 0;
        return result;
    }

    void resize() {
        capacity *= 2;
        int *new_array = new int[capacity];
        for (int i = 0; i < size; i++)
        {
            new_array[i] = array[i];
        }
        array = new_array;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};
