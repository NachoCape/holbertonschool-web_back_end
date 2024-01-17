export default function appendToEachArrayValue(array, appendString) {
    for (const [i, elem] of array.entries()) {
        array[i] = appendString + elem;
    }
    return array;
  }