import java.util.Scanner;
public class slope_style_score {
	public static void main(String[] args){
		System.out.print("Input number of judges: ");
		Scanner input = new Scanner(System.in);
		int number_of_judges = input.nextInt();
		int[] score = new int[number_of_judges];
		for(int i=0; i<number_of_judges; i++){
			System.out.printf("\nEnter judge number %d score: ", i+1);
			score[i] = input.nextInt();
		}
		System.out.print("The final score of the contestor is: ");
		System.out.println(calculate_score(score));
	}
	
	public static double calculate_score(int scores[]){
		int  max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;
		double sum = 0;
		for(int i=0; i<scores.length; i++){
			if(scores[i]>max){
				max = scores[i];
			}
			if(scores[i]<min){
				min = scores[i];
			}
			sum += scores[i];
		}
		sum -= (min+max);
		sum /= (scores.length-2);
		double roundet = Math.round(sum * 100) /100.0;
		return roundet;
	}
}
