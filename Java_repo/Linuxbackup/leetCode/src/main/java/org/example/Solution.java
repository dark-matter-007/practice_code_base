package org.example;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> duplicateIntegerList = new ArrayList<>() ;

        List<Integer> encounteredNumbersStack = new ArrayList<Integer>();

        for ( int number : nums ) {
            if ( encounteredNumbersStack.contains(number) ) { // this number was found earlier
                duplicateIntegerList.add(number);
            }
            encounteredNumbersStack.add(number);
        }

        return duplicateIntegerList;
    }
}