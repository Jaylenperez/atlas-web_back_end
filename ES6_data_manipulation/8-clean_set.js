export default function cleanSet(set, startString) {
  if (startString === '') return ''; // Return an empty string if startString is empty

  return Array.from(set)
    .filter((value) => value.startsWith(startString)) // Filter values that start with startString
    .map((value) => value.slice(startString.length)) // Remove startString from the beginning of each value
    .join('-'); // Join the remaining values with '-'
}
