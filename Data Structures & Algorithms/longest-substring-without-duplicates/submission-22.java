class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character,Integer> mySet = new HashMap<>();
        char[] converted = s.toCharArray();
        int i = 0 , j = 0  , longest = 0, current =0  ;
        int len = converted.length;
        while(i < len ){
            // zxybxzyz
            ////abcdeedba
            if(mySet.containsKey(converted[i])){
                j = mySet.get(converted[i]) + 1 ;
                mySet.clear();
                for(int k = j ; k <= i ; k++){
                    mySet.put(converted[k], k);
                }
            }
            else{
                mySet.put(converted[i], i);
            }
            current = i - j + 1 ; 
            if(current >= longest){
                longest  = current;
            }
            i++;
        }
        return longest;
    }
}
