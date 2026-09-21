This code was used in the project titled EDP (Encryption Decryption Protocol) to store file paths inside an envelope for file restoration purposes.

How it works:
  Packing a piece of data finds the path of the file and stores that along with a prefix number that determines the count of characters in the path. 
  Unpacking the packed piece of data will read the number and, correlating that with the path, then remove the path and use that to point the file restoration location.
