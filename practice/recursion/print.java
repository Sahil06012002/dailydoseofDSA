class Main {

    public void print(int n) {
        if (n == 5) {
            System.out.println(n);
            return;
        }
        System.out.println(n);
        print(n+1);
    }

    public static void main(String[] args) {
        Main sol = new Main();
        sol.print(1);
    }
}