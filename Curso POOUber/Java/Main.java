class Main {
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        UberX uberX = new UberX("AMQ123", new Account("Andres Herrera", "AND123"), "Chevrolet", "Sonic");
        //uberX.passenger = 4;
        uberX.setPassenger(3);
        uberX.printDataCar(); 
    
        /*Car car2 = new Car("RMX025", new Account("Andrea Herrera", "TWX478"));
        car2.passenger = 2;
        car2.printDataCar();*/
    }
}   