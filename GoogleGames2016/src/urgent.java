
import java.io.IOException;
import javax.xml.bind.DatatypeConverter;
import java.io.UnsupportedEncodingException;

import sun.misc.*;

public class urgent {
	public static void main(String[] args) throws IOException{		
	    String base64_str = "8hryGgSEprb2FgSehu4ETq72ngR29gTWNpa2BKYWLgQupuZO9mYELuR29il";
	    byte[] decode = DatatypeConverter.parseBase64Binary(base64_str);

	    StringBuilder sb = new StringBuilder();
	    for (int i = 0; i < decode.length; i++){
	        String temp = Integer.toBinaryString(decode[i]);
	        sb.append(String.format("%8s", temp).replace(" ", "0"));
	    }

	    String binary = sb.toString();
	    //System.out.println(binary.length());
		
	    
	    for(int i = 0; i < binary.length() / 8; i++){
	    	String curChar = "";
	    	String bin = "";
	    	for(int c = 0; c < 8; c++){
	    		curChar += binary.charAt(8 * i + c);
	    	}
	    	for(int c = 0; c < 8; c++){
	    		//reverse
	    		bin += curChar.charAt(7 - c);
	    	}
    	    int charCode = Integer.parseInt(bin, 2);
    	    String str = new Character((char)charCode).toString();
    	    System.out.print(str);
	    }
	}

}
