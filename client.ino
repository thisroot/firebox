
const byte buffSize = 40;
const int pin =  3;
char inputBuffer[buffSize];

const char startMarker = '<';
const char endMarker = '>';
byte bytesRecvd = 0;
boolean readInProgress = false;
boolean newDataFromPC = false;

char messageFromPC[buffSize] = {0};
char index1[buffSize] = {0};
char index2[buffSize] = {0};
char deviceName[] = "stimulator";
int timing;



//=============

void setup() {
  Serial.begin(19200);
  pinMode(pin, OUTPUT);           // set pin to input
   
    // tell the PC we are ready
  Serial.println("<Arduino is ready>");
}

void pulseLed() {
   digitalWrite(pin, HIGH);        // sets the pin on
   delay(200);        // pauses for 50 microseconds      
   digitalWrite(pin, LOW);         // sets the pin off
   delay(200);       // pauses for 50 microseconds
  }

void LedHigh(int timing){
   digitalWrite(pin, HIGH); // sets the pin on
   delay(timing);           // pauses for 50 microseconds
}

void LedLow(){
   digitalWrite(pin, LOW);         // sets the pin off
   delay(200);       // pauses for 50 microseconds
  }

//=============
 
void parseData() {

    // split the data into its parts
  char * strtokIndx; // this is used by strtok() as an index
  
  strtokIndx = strtok(inputBuffer,",");      // get the first part - the string
  strcpy(messageFromPC, strtokIndx); // copy it to messageFromPC
  
  strtokIndx = strtok(NULL, ","); // this continues where the previous call left off
  timing = atoi(strtokIndx);
  //strcpy(index1, strtokIndx);     // convert this part to an integer

  strtokIndx = strtok(inputBuffer, ","); // this continues where the previous call left off
  strcpy(index2, strtokIndx);     // convert this part to an integer
  // for int
  //strtokIndx = strtok(NULL, ","); 
  //index2 = atof(strtokIndx);     // convert this part to a float

}

//=============

void getDataFromPC() {

    // receive data from PC and save it into inputBuffer
    
  if(Serial.available() > 0) {

    char x = Serial.read();

      // the order of these IF clauses is significant
      
    if (x == endMarker) {
      readInProgress = false;
      newDataFromPC = true;
      inputBuffer[bytesRecvd] = 0;
      parseData();
    }
    
    if(readInProgress) {
      inputBuffer[bytesRecvd] = x;
      bytesRecvd ++;
      if (bytesRecvd == buffSize) {
        bytesRecvd = buffSize - 1;
      }
    }

    if (x == startMarker) { 
      bytesRecvd = 0; 
      readInProgress = true;
    }
  }
}


//=============

void replyToPC() {

  if (newDataFromPC) {
    newDataFromPC = false;
    Serial.print("<");
    if (strcmp(messageFromPC, "getName")  == 0) {
      Serial.print(deviceName);
    }

    if (strcmp(messageFromPC, "fire")  == 0) {
      LedHigh(timing);
      Serial.print("fired");
    }
    
    Serial.println(">");
  }
}

//=============

void loop() {
  getDataFromPC();
  replyToPC();
}

//=============
