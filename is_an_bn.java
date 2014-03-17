import java.util.Scanner;
public class is_an_bn {
	public static void main(String[] args){
		System.out.println("Enter a word: ");
		Scanner input = new Scanner(System.in);
		String some_word = input.next();
		System.out.println(an_bn_word(some_word));
	}
	public static String an_bn_word(String word){
		int len = word.length();
		String first_part;
		String second_part;
		int token = len / 2;
		if(len % 2 == 0){
			first_part = word.substring(0, token);
			second_part = word.substring(token, word.length());
		}
		else{
			return "Not an an bn word!";
		}
		for(int i=0; i<first_part.length(); i++){
			
			if(first_part.charAt(i) != 97){
				return "Not an an bn word!";
			}
		}
		for(int i=0; i<second_part.length(); i++){
			if(second_part.charAt(i) != 98){
				return "Not an an bn word!";
			}
		}
		return "It is an an bn word!";
	}	
}
