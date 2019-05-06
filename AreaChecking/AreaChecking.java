import java.util.Random;
public class AreaCheck {
  //ruhunukumari
  static int users = 4;
  static int model = 10;
  
  public static void main(String[] args) {    
    Random rand = new Random(); 
    int [][] matrix = new int [users][users];
    int a = (matrix.length);
    int b = (matrix[0].length);
    
    //Set the Blank
    for(int i = 0; i < a; i++) {
      for(int j = 0; j < b; j++) {
        int n = rand.nextInt(500);
        //Set the blanks
        if(i == j) {
          matrix[i][j] = 0;
        }
        //Set other values  
        if((i < j) && (Integer.parseInt(Integer.toString(i) 
			+ Integer.toString(j)) < model)) {
          matrix[i][j] = n;
          matrix[j][i] = n;
        }
      }
      model = model + 10;
    }
    //Print
    for (int i = 0; i<matrix.length; i++) {
        for (int j = 0; j<matrix[i].length; j++) {
            System.out.print(matrix[i][j] + "\t");
        }
        System.out.println();
    }  
  }
}
