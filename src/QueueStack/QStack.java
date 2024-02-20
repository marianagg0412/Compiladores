package QueueStack;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class QStack implements ILista{

    private Stack<Integer> s;

    @Override
    public void add(int e) {
        s.push(e);
    }

    public QStack(Stack<Integer> s) {
        this.s = s;
    }

    @Override
    public int rm() {
        return s.pop();
    }
}
