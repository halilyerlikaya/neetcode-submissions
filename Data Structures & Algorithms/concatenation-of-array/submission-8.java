class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] doubl = new int[2*nums.length];
        int j = 0;
        for( int i : nums){
            doubl[j] = doubl[j + nums.length] = i ;
            j++;
        }
        return doubl;
    }
}