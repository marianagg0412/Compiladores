package QueueStack;

import java.util.LinkedList;
import java.util.Queue;

public class QQueue implements ILista{
    private Queue<Integer> q;


    @Override
    public void add(int e) {
        q.add(e);
    }

    public QQueue(Queue<Integer> q) {
        this.q = q;
    }

    @Override
    public int rm() {
        return q.poll();
    }
}
