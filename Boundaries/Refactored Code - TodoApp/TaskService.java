import java.util.ArrayList;
import java.util.List;

public class TaskService {
    private final List<Task> tasks = new ArrayList<>();

    public void addTask(String taskName) {
        tasks.add(new Task(taskName));
    }

    public boolean removeTask(int index) {
        if (isValidIndex(index)) {
            tasks.remove(index);
            return true;
        }
        return false;
    }

    public boolean markTaskDone(int index) {
        if (isValidIndex(index)) {
            tasks.get(index).markDone();
            return true;
        }
        return false;
    }

    public List<Task> getTasks() {
        return tasks;
    }

    private boolean isValidIndex(int index) {
        return index >= 0 && index < tasks.size();
    }

    public boolean isEmpty() {
        return tasks.isEmpty();
    }
}
