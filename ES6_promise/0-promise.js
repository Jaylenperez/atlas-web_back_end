// 0-promise.js
function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Response from API");
        }, 1000);
    });
}

export default getResponseFromAPI;