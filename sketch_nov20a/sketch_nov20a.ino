#include <SoftwareSerial.h>
SoftwareSerial co2Serial(A0, A1);

void setup() {
  Serial.begin(9600);
  co2Serial.begin(9600);
}

void loop() {
  byte cmd[9] = {0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x79};
  unsigned char response[9];
  co2Serial.write(cmd, 9);
  co2Serial.readBytes(response, 9);
  if (response[0] != 0xFF) {
    return 0;
  }
  if (response[1] != 0x86) {
    return 0;
  }
  unsigned int responseHigh = (unsigned int) response[2];
  unsigned int responseLow = (unsigned int) response[3];
  delay(100);
  Serial.println(ppm);

  delay(1);
}
