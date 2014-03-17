import java.util.Scanner;


public class prepare_meal {
	public static void main(String[] args){
		System.out.println("Please input an integer: ");
		Scanner input = new Scanner(System.in);
		int input_number = input.nextInt();
		System.out.println(spam_and_eggs(input_number));
	}
	public static String spam_and_eggs(int number){
		boolean eggs = false;
		StringBuilder spam = new StringBuilder();
		if(number % 5 == 0){
			eggs = true;
			number /= 5;
		}
		int count = 0;
		while(number>2){
			if(number % 3 != 0){
				break;
			}
			else{
				number /= 3;
				count++;
			}
		}
		if(count>0){
			for(int i=0; i<count; i++){
				spam.append("spam ");
			}
			if(eggs){
				spam.append("and eggs");
			}
			return spam.toString();
		}
		else{
			if(eggs){
				return "eggs";
			}
			else{
				return "\"\"";
			}
		}
	}
}
