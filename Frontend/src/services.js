const API = "http://127.0.0.1:5000/";

export const transformMidiToMp3 = (input_midi) => {
  return fetch(API + "midi/convertToMP3", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    //send content from input input-midi
    body: input_midi,
  })
    .then((response) => response.json())
    .then((data) => {
      const { url_file } = data;
      return API + url_file;
    });
};
