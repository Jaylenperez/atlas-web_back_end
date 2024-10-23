function signUpUser(firstName, lastName) {
  // Return a resolved promise with the desired object structure.
  return Promise.resolve({
    firstName,
    lastName,
  });
}

export default signUpUser;
