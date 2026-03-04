package practice.CustomDataStructures;

import java.util.ArrayList;

public class CustomStack {
    private int ptr = -1;
    private ArrayList<Integer> stack = new ArrayList<>();
    private ArrayList<Integer> minStack = new ArrayList<>();

    public int push(int element) {
        stack.add(element);
        if (minStack.isEmpty() || minStack.get(minStack.size() - 1) >= element) {
            minStack.add(element);
        } else {
            minStack.add(minStack.get(minStack.size() - 1));
        }
        return element;
    }

    public int pop() throws Exception {
        if (isEmpty()) {
            throw new Exception("Stack is Empty");
        }
        return stack.remove(ptr--);
    }

    public int peek() throws Exception {
        if (isEmpty()) {
            throw new Exception("Stack is Empty");

        }
        return stack.get(ptr);
    }

    public boolean isEmpty() {
        return ptr == -1;
    }

    public int getMin() throws Exception {
        int min = Integer.MAX_VALUE;
        if (isEmpty()) {
            throw new Exception("Stack is Empty");

        }
        for (int i = 0; i < stack.size(); i++) {
            min = Math.min(min, stack.get(i));

        }
        return min;
    }

}
