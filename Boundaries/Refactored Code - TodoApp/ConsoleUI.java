import java.util.List;
import java.util.Scanner;

public class ConsoleUI {
    private final Scanner scanner = new Scanner(System.in);
    private final TaskService taskService;

    public ConsoleUI(TaskService taskService) {
        this.taskService = taskService;
    }

    public void run() {
        while (true) {
            printMenu();
            int choice = getUserChoice();

            switch (choice) {
                case 1 -> handleAddTask();
                case 2 -> handleRemoveTask();
                case 3 -> handleMarkTaskDone();
                case 4 -> listTasks();
                case 5 -> {
                    System.out.println("Bye!");
                    return;
                }
                default -> System.out.println("Invalid option. Try again.");
            }
        }
    }

    private void printMenu() {
        System.out.println("\n1. Add Task");
        System.out.println("2. Remove Task");
        System.out.println("3. Mark Task as Done");
        System.out.println("4. List Tasks");
        System.out.println("5. Exit");
        System.out.print("> ");
    }

    private int getUserChoice() {
        try {
            return Integer.parseInt(scanner.nextLine().trim());
        } catch (NumberFormatException e) {
            return -1;
        }
    }

    private void handleAddTask() {
        System.out.print("Enter task: ");
        String taskName = scanner.nextLine().trim();
        if (!taskName.isEmpty()) {
            taskService.addTask(taskName);
            System.out.println("Task added.");
        } else {
            System.out.println("Task cannot be empty.");
        }
    }

    private void handleRemoveTask() {
        if (taskService.isEmpty()) {
            System.out.println("No tasks to remove.");
            return;
        }

        listTasks();
        int index = getTaskIndex("Enter task number to remove: ");
        if (taskService.removeTask(index)) {
            System.out.println("Task removed.");
        } else {
            System.out.println("Invalid task number.");
        }
    }

    private void handleMarkTaskDone() {
        if (taskService.isEmpty()) {
            System.out.println("No tasks to mark.");
            return;
        }

        listTasks();
        int index = getTaskIndex("Enter task number to mark as done: ");
        if (taskService.markTaskDone(index)) {
            System.out.println("Task marked as done.");
        } else {
            System.out.println("Invalid task number.");
        }
    }

    private void listTasks() {
        List<Task> tasks = taskService.getTasks();
        if (tasks.isEmpty()) {
            System.out.println("No tasks available.");
        } else {
            for (int i = 0; i < tasks.size(); i++) {
                System.out.println((i + 1) + ". " + tasks.get(i));
            }
        }
    }

    private int getTaskIndex(String prompt) {
        System.out.print(prompt);
        try {
            return Integer.parseInt(scanner.nextLine().trim()) - 1;
        } catch (NumberFormatException e) {
            return -1;
        }
    }
}
