export default function taskBlock(trueOrFalse) {
  const task = false; // Initial value for task
  const task2 = true; // Initial value for task2

  if (trueOrFalse) {
    const task = true;
    const task2 = false;
    console.log(task + task2);
  }

  return [task, task2];
}
