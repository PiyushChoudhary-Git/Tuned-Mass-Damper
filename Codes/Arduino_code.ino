#include <MPU9250_asukiaaa.h>
#include <Adafruit_BMP280.h>

#ifdef _ESP32_HAL_I2C_H_
#define SDA_PIN 21
#define SCL_PIN 22
#endif

Adafruit_BMP280 bmp;
MPU9250_asukiaaa mySensor;

float aX, aY, aZ, aSqrt;

void setup()
{
  Serial.begin(115200);
  while (!Serial)
    ;

#ifdef _ESP32_HAL_I2C_H_
  Wire.begin(SDA_PIN, SCL_PIN);
  mySensor.setWire(&Wire);
#else
  Wire.begin();
  mySensor.setWire(&Wire);
#endif
  bmp.begin();
  mySensor.beginAccel();
}

void loop()
{
  if (mySensor.accelUpdate() == 0)
  {
    aX = mySensor.accelX();
    aY = mySensor.accelY();
    aZ = mySensor.accelZ();
    aSqrt = mySensor.accelSqrt();

    Serial.print(String(aX));
    Serial.print("\t" + String(aY));
    Serial.print("\t" + String(aZ));
    Serial.println();
  }

  delay(50);
}
