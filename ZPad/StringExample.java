//package arrexample;

public class StringExample {
    public static void main(String[] args) {
        String[] strArr =new String[2];

        strArr[0] ="Hello";
        strArr[1] ="Ram";
        strArr[2]="Hari";


        for (int i = 0; i < strArr.length; i++) {

            if(strArr[i]=="Ram"){
                System.out.println("Ram is in"+i+"index");
            }

        }
    }
}