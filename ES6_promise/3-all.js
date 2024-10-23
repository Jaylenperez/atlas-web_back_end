import { uploadPhoto, createUser } from './utils';

async function handleProfileSignup() {
  try {
    // Collectively resolve the promises from uploadPhoto and createUser
    const [photo, user] = await Promise.all([uploadPhoto(), createUser()]);

    // Log the firstName and lastName from the user object
    console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
  } catch (error) {
    // Log an error message if any of the promises fail
    console.log('Signup system offline');
  }
}

export default handleProfileSignup;
