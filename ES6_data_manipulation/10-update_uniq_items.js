export default function updateUniqueItems(map) {
    // Check if the argument is a Map
    if (!(map instanceof Map)) {
        throw new Error('Cannot process');
    }

    // Iterate through the entries of the Map
    for (const [key, value] of map.entries()) {
        // Update the quantity if it is 1
        if (value === 1) {
            map.set(key, 100); // Set the new quantity to 100
        }
    }
}
