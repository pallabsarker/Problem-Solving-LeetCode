class Solution {
    public boolean isPalindrome(int n) {
        int x, digit, rev = 0;
        if(n < 0) return false;
        else{
            x = n;
            while(x != 0){
                digit = x % 10;
                rev = (rev * 10) + digit;
                x /= 10;
            }
            if(rev == n) return true;
            else return false;
        }
    }
}
