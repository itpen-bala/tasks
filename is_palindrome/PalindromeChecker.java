import java.util.Scanner;

class PalindromeChecker {

    public static boolean isPalindrome(String word) {

        for(int i = 0; i < word.length() / 2; i++) {
            if(word.charAt(i) != word.charAt(word.length() - 1 - i))
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the word: ");
        String word = input.nextLine();

        System.out.println("Word \'" + word + "\' is palindrome: " + isPalindrome(word));
    }
}
