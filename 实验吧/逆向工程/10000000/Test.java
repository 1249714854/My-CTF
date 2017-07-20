package test;

public class Test {

	public static void main(String[] args) {
		char[] v = new char[13];
		v[0] = (char) 0x0e6;
		v[1] = (char) 0x0ec;
		v[2] = (char) 0x0e1;
		v[3] = (char) 0x0e7;
		v[4] = (char) 0x0ba;
		v[5] = (char) 0x0f4;
		v[6] = (char) 0x0e5;
		v[7] = (char) 0x0f3;
		v[8] = (char) 0x0f4;
		v[9] = (char) 0x0f4;
		v[10]= (char) 0x0e5;
		v[11]= (char) 0x0f3;
		v[12]= (char) 0x0f4;
		char[] s = new char[13];
		for(int i=0; i<13; i++)
			s[i] = (char) (v[i] & 0x80);
		System.out.println(s);
		for(int i=0; i<13; i++)
			s[i] = (char) (v[i] ^ 0x80);
		System.out.println(s);
	}

}
