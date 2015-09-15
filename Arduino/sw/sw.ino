const int sw=8, led_out=13, led_status=11;
boolean c,p=0, ledS;


void setup()
{
  pinMode(sw,INPUT);
  pinMode(led_out, OUTPUT);
  pinMode(led_status, INPUT);
  
}

void loop()
{
  c=debRead();
  if(p==0 && c==1)
    {
     ledS=digitalRead(led_status);
     ledS = !ledS;
     digitalWrite(led_out, ledS);
     
    }
  p=c;
  
}  
  
boolean debRead()
{
  boolean a,b;
  while(1)
  {
    a=digitalRead(sw);
    delay(5);
    b=digitalRead(sw);
    if(a==b)
      return a;
  }
}
