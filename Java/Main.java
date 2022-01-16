class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");

        Car car = new Car("AMQ-123", new Account("Luis Rueda", "70059584"));
        Car car2 = new Car("AN-1212", new Account("Karen Moril", "70313165"));
        car.passenger = 4;
        car2.passenger = 3;
        car.printDataCar();
        car2.printDataCar();
    }
}