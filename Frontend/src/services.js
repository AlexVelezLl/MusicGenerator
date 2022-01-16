const API = "http://127.0.0.1:5000/";

export const transformMidiToMp3 = async (input_midi) => {
  const response = await fetch(API + "midi/convertToMP3", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: input_midi,
  });
  const data = await response.json();
  return API + data.url_file;
};

export const generateMelody = async ({
  seedName,
  note,
  mode,
  temperature,
  tempo,
}) => {
  const response = await fetch(API + "generateMelody", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json"
    },
    body: JSON.stringify({
      midi_file: seedName,
      note,
      mode,
      temperature,
      tempo
    }),
  });
  const data = await response.json();
  if(response.status === 200) {
    return {
      midiFile: API + data.midiFile,
      mp3File: API + data.mp3File,
    }
  }
  throw data.message;
}
