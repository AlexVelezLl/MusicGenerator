import React, { useState } from 'react';
import Header from './Header';
import SeedMusic from './seedMusic';
import OutputMusic from './outputMusic';

import './index.scss';
import { modes, notes } from '../constants';
import { generateMelody } from '../services';

const App = () => {
  const [seedName, setSeedName] = useState('');
  const [outputMidi, setOutputMidi] = useState('');
  const [outputMP3, setOutputMP3] = useState('');
  const [note, setNote] = useState(notes[0]);
  const [mode, setMode] = useState(modes[0]);
  const [temperature, setTemperature] = useState(20);
  const [outputLoading, setOutputLoading] = useState(false);
  const handleGenerateMelody = async () => {
    setOutputLoading(true);
    try{
      const response = await generateMelody({
        seedName,
        note: note.value,
        mode: mode.value,
        temperature: temperature/100,
      });
      setOutputMidi(response.midiFile);
      setOutputMP3(response.mp3File);
      setOutputLoading(false);
    } catch (error) {
      console.log(error);
      setOutputLoading(false);
    }
  }
  return (
    <div className="App">
      <Header />
      <SeedMusic 
        setSeedName={setSeedName}
        note={note}
        setNote={setNote}
        mode={mode}
        setMode={setMode}
        temperature={temperature}
        setTemperature={setTemperature}
      />
      <div className="generate-music-container">
        <button 
          className='btn'
          onClick={handleGenerateMelody}
        >
          GENERATE MUSIC
        </button>
      </div>
      <OutputMusic 
        outputMidi={outputMidi}
        outputMP3={outputMP3}
        outputLoading={outputLoading}
      />
    </div>
  );
}

export default App;
