#include <stdio.h>

main(int argv, char *argc[]){
  int a,b,c,d,e,f,g,h,i;
  
  a=1;
  b=84*100+100000;
  c=b+17000;
  d=2;
  e=2;
  f=1;
  g=0;
  h=0;
  
  for (i=b;i<=c;i+=17){
    f=1;
    //  This direct translation of assembly works... but the f!=0 bit is not enough
    // of an optimization, it is still very very slow.
    //e=2;
    // while(e-i != 0 && f!=0) {
    //   d=2;
    //   while(d-i != 0 && f!=0){
    //     if (d*e-i==0) { f=0; }
    //     d++;
    //     }
    //   e++;
    // }
    
    //  Modulus on a single loop, plus f!=0 shortcut is much faster
    d=2;
    while(d-i != 0 && f!=0){
      if (i%d == 0 ) {f=0;}
      d++;
    }
  if (f==0) {
    h++;
  }
  else{
    printf("%d is prime\n",i);
  }
  }
  printf("The Value in register h is %d\n",h);
}