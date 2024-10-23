import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
    try {
      const promise = signUpUser(firstName, lastName);
      const photo = uploadPhoto(fileName);
  
      const [result, newPhoto] = await Promise.allSettled([promise, photo]);
  
      return [
        { status: result.status, value: result.status === 'fulfilled' ? result.value : result.reason },
        { 
          status: newPhoto.status, 
          value: newPhoto.status === 'fulfilled' 
            ? newPhoto.value 
            : (newPhoto.reason instanceof Error ? newPhoto.reason.message : newPhoto.reason) 
        },
      ];
    } catch (error) {
      console.error('error error error', error);
      return [];
    }
  }
  