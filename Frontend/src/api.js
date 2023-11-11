export const SERVER_URL = "http://127.0.0.1:5000"; // flask server URL

export function parseUserInstr(prompt) {
  return fetch(`${SERVER_URL}/prompt=${prompt}`).then((response) =>
    response.json()
  );
}
