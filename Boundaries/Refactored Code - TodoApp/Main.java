public class Main {
    public static void main(String[] args) {
        TaskService taskService = new TaskService();
        ConsoleUI ui = new ConsoleUI(taskService);
        ui.run();
    }
}
