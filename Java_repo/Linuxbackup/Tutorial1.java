public class Tutorial1 {
    public static void main(String arguments[]) {

//        String myNumber = "23";
//        Integer sum = Integer.parseInt(myNumber) + 34;
//
//        System.out.println("hello" + " world " + sum);
//
//        Car car = new BMW(120, 34, false);
//        car.accelarate();
//
        BMW car = new Loki(120);
        Car bmwWaliCar = new BMW(50);

        bmwWaliCar.accelarate();
        car.accelarate();

        System.out.println(car.getSpeed());
        System.out.println(bmwWaliCar.getSpeed());
    }
}


abstract class Car{
    public String glassTint = "black";

    private int speed;
    private String engineVariant;
    private int decelaration;
    private float maxSteerAngle;
    private boolean isJDM;

    public Car(int speed, int decelaration, boolean isJDM) {
        this.speed = speed;
        this.decelaration = decelaration;
        this.isJDM = isJDM;
    }

    public Car(int speed) {
        this.speed = speed;
    }


    public void accelarate() {
        this.speed += 2;
    }

    public void accelarate(int value) {
        this.speed += value;
    }


    public int getSpeed() {
        return this.speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    public int getDecelaration() {
        return decelaration;
    }

    public void setDecelaration(int decelaration) {
        this.decelaration = decelaration;
    }

    public float getMaxSteerAngle() {
        return maxSteerAngle;
    }

    public void setMaxSteerAngle(float maxSteerAngle) {
        this.maxSteerAngle = maxSteerAngle;
    }

    public boolean isJDM() {
        return isJDM;
    }

    public void setJDM(boolean JDM) {
        isJDM = JDM;
    }
}

class GoCart extends Car {

    boolean openHeaded;

    public GoCart(int speed, int decelaration, boolean isJDM) {
        super(speed, decelaration, isJDM);
    }



}


class BMW extends  Car {

    @Override
    public void accelarate() {
        super.accelarate(4);
    }

    public BMW(int speed, int decelaration, boolean isJDM) {
        super(speed, decelaration, isJDM);
    }

    public BMW (int speed) {
        super(speed);
    }

}

class Loki extends BMW {

    public Loki(int speed, int decelaration, boolean isJDM) {
        super(speed, decelaration, isJDM);
    }

    public Loki (int speed) {
        super(speed);
    }

    @Override
    public void accelarate() {
        super.accelarate(6);
    }
}
