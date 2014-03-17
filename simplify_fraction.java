import java.util.Scanner;
public class simplify_fraction {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.println("Input numerator: ");
		int numerator = input.nextInt();
		System.out.println("Input denominator: ");
		int denominator = input.nextInt();
		int simple_fraction[] = simplified_fraction(numerator, denominator);
		System.out.println("The simplified fraction is: " + simple_fraction[0] + 
								"/" + simple_fraction[1]);
		
	}
	public static int[] simplified_fraction(int a, int b){
		int divisor = gcd(a, b);
		int simplified_fraction[] = {a/divisor, b/divisor};
		return simplified_fraction;
	}
	
	public static int gcd(int a, int b){
		int max = a;
		if(a<b){
			a = b;
			b = max;
		}
		max = 0;
		for(int i=1; i<b+1; i++){
			if((a%i==0) && (b%i == 0) ){
				max = i;
			}
		}
		return max;
	}
}

