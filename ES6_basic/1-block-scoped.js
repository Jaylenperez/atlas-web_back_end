export default function taskBlock(trueOrFalse) {
  const task = false; // Changed from var to let
  const task2 = true; // Changed from var to let

  if (trueOrFalse) {
    const task = true; // New block-scoped variable
    const task2 = false; // New block-scoped variable
  }

  return [task, task2];
}
