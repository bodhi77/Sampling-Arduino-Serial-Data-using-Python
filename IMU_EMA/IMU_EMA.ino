#include<Wire.h>
const int MPU_addr = 0x68;
int16_t AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ;
int minVal = 265;
int maxVal = 402;
double sdtX = 0, sdtY = 0, sdtZ = 0;
float alpha=0.05;
double xf, xnf;
double yf, ynf;
double zf, znf;

void setup(){
Wire.begin();
Wire.beginTransmission(MPU_addr);
Wire.write(0x6B);
Wire.write(0);
Wire.endTransmission(true);

Serial.begin(115200);
delay(2000);

}
void loop(){

Wire.beginTransmission(MPU_addr);
Wire.write(0x3B); // Alamat accelerometer
Wire.endTransmission(false);
Wire.requestFrom(MPU_addr, 14, true);
AcX=Wire.read()<<8|Wire.read();
AcY=Wire.read()<<8|Wire.read();
AcZ=Wire.read()<<8|Wire.read();
int sdX = map(AcX, minVal, maxVal, -90, 90);
int sdY = map(AcY, minVal, maxVal, -90, 90);
int sdZ = map(AcZ, minVal, maxVal, -90, 90);
sdtX = alpha*sdX + (1-alpha)*sdtX;
sdtY = alpha*sdY + (1-alpha)*sdtY;
sdtZ = alpha*sdZ + (1-alpha)*sdtZ;

xnf= RAD_TO_DEG * (atan2(-sdY, - sdZ) + PI);
ynf = RAD_TO_DEG * (atan2(-sdX, - sdZ) + PI);
znf= RAD_TO_DEG * (atan2(-sdY, - sdX) + PI);
xf= RAD_TO_DEG * (atan2(-sdtY, - sdtZ) + PI);
yf = RAD_TO_DEG * (atan2(-sdtX, - sdtZ) + PI);
zf= RAD_TO_DEG * (atan2(-sdtY, - sdtX) + PI);

  Serial.print(xnf);
  Serial.print(",");
  Serial.println(xf);
//  Serial.print(",");
//  Serial.print(ynf);
//  Serial.print(",");
//  Serial.print(yf);
//  Serial.print(",");
//  Serial.print(znf);
//  Serial.print(",");
//  Serial.println(zf);
  delay(10);

}
