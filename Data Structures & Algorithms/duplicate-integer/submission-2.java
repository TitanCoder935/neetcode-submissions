// import java.util.HashMap;

class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer,Integer> dic= new HashMap<>();
        for(int i=0; i < nums.length ; i++){
            if( dic.containsKey(nums[i])){
                return true;
            }else{
                dic.put(nums[i],nums[i]);
            }   
        }
        return false;
    }
}