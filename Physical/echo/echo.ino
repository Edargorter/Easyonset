/*
* Ultrasonic Sensor HC-SR04 and Arduino Tutorial
*
* by Dejan Nedelkovski,
* www.HowToMechatronics.com
*
*/
// defines pins numbers
const int trigPin = 10;
const int echoPin = 9;
// defines variables
long duration;
double distance;
int dists = 0;
double temp_sum;
double temp_dist;
double values[10];
int act_values[] = {5, 10, 20, 30, 40, 50, 60, 70, 80, 90};
void setup() {
pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
Serial.begin(9600); // Starts the serial communication
}

void loop() {
  Serial.println(dists);
  delay(5000);
  temp_sum = 0.0;
  for(int i = 0; i < 100; i += 1){
    // Clears the trigPin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);
    // Calculating the distance
    temp_dist = duration*0.034/2;
    temp_sum += temp_dist;
  }
  distance = temp_sum / 100.0;
  if(dists < 10){
    values[dists] = distance;
  } else {
    for(int i = 0; i < 10; i += 1){
      String data = String(act_values[i]) + " " + String(values[i]);
      Serial.println(data);
    }
  }
  dists += 1;
}
