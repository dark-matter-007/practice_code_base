package org.example;

public class BinaryAdder {
    private  String expression1;
    private  String expression2;

    public String sum() {
        int len1 = expression1.length();
        int len2 = expression2.length();
        int largerLength = Math.max(len1, len2);
        StringBuilder result = new StringBuilder();

        for ( int i = (largerLength-1); i >= 0; i-- ) {
            char char1;
            try {
                char1 = expression1.charAt(i);
            } catch(Exception e) {
                char1 = '0';
            }
            char char2;
            try {
                char2 = expression2.charAt(i);
            } catch(Exception e) {
                char2 = '0';
            }
            result.append((char1 == '1' || char2 == '1') ? "1" : "0");
        }

        return result.reverse().toString();
    }

//   GETTERS AND SETTERS
    public String getExpression1() {
        return expression1;
    }

    public void setExpression1(String expression1) {
        this.expression1 = expression1;
    }

    public String getExpression2() {
        return expression2;
    }

    public void setExpression2(String expression2) {
        this.expression2 = expression2;
    }
}
