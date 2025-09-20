using System;  

public class ArrayExample  
{  
    public static void Main(string[] args)  
    {  
        int[] arr = new int[5];//creating array  
        arr[0] = 10;//initializing array  
        arr[2] = 20;  
        arr[4] = 30;  
  
        //traversing array  
        for (int i = 0; i < arr.Length; i++)  
        {  
            Console.WriteLine(arr[i]);  
        }  
    }  
} 
