// Project: Direct 1:1 control of a 180° servo using a single potentiometer
// Author: Dae
// Platform: ESP32 (Arduino core)

#include <ESP32Servo.h>   // Library that provides servo control on the ESP32

Servo myServo;          // Create a Servo object to control the servo

// Pin assignments
const int potPin = 34;    // ADC input pin for the potentiometer (analog read only)
const int servoPin = 18;  // PWM output pin for the servo signal

void setup() {
  Serial.begin(115200);   // Initialize serial port for monitoring at 115200 baud
  delay(1000);            // Short delay to allow serial monitor to open/stabilize

  // Attach the servo object to the servoPin.
  // The additional parameters define the valid pulse width range in microseconds.
  // Typical hobby servos accept pulses in the range ~500 to ~2400 µs.
  myServo.attach(servoPin, 500, 2400);
}

void loop() {
  // Read the raw ADC value from the potentiometer.
  // On the ESP32 Arduino core this returns 0..4095 for 12-bit resolution.
  int raw = analogRead(potPin);

  // Map the raw ADC range (0..4095) to the servo angle range (0..180).
  // map() returns a long integer; we store the mapped value in an int 'angle'.
  int angle = map(raw, 0, 4095, 0, 180);

  // Command the servo to move to the computed angle (degrees).
  myServo.write(angle);

  // Print raw ADC value and mapped angle for debugging/monitoring.
  Serial.print("Raw: ");
  Serial.print(raw);
  Serial.print(" | Angle: ");
  Serial.println(angle);

  // Small delay to stabilize sampling and reduce jitter.
  delay(20);
}

