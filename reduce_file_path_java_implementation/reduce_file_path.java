import java.util.Scanner;
public class reduce_file_path {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.println("Input a path: ");
		String path = input.next();
		System.out.println("The reduced path is: ");
		System.out.println(reduce_path(path) );
	}
	
	public static String reduce_path(String path){
		path = path.replace("//", "/");
		path = path.replace("/./", "/");
		String[] folders = path.split("/");
		StringBuilder new_string = new StringBuilder();
		for(int i=0; i<folders.length; i++){
			if(folders[i].equals("..")){
				folders[i] = "";
				folders[i-1] = "";
			}
		}
		for(int i=0; i<folders.length; i++){
			if( !folders[i].equals("")){
				new_string.append(folders[i] + "/");
			}
		}
		new_string.setLength(new_string.length() - 1);
		return new_string.toString();
	}
}
