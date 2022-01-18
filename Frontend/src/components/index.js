import React, { useState } from 'react';
import Header from './Header';
import Collapse from '@mui/material/Collapse';
import Alert from '@mui/material/Alert';
import CloseIcon from '@mui/icons-material/Close';
import IconButton from '@mui/material/IconButton';

import SeedMusic from './seedMusic';
import OutputMusic from './outputMusic';
import { modes, notes, tempos } from '../constants';
import { generateMelody } from '../services';

import './index.scss';

const App = () => {
  const [seedName, setSeedName] = useState('');
  const [outputMidi, setOutputMidi] = useState('');
  const [outputMP3, setOutputMP3] = useState('');
  const [note, setNote] = useState(notes[0]);
  const [mode, setMode] = useState(modes[0]);
  const [tempo, setTempo] = useState(tempos[2]); // Default 120 BPM 
  const [temperature, setTemperature] = useState(20);
  const [outputLoading, setOutputLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const handleGenerateMelody = async () => {
    if(!seedName) {
      return setErrorMessage('You have to select a seed');
    }
    setOutputLoading(true);
    try{
      const response = await generateMelody({
        seedName,
        note: note.value,
        mode: mode.value,
        temperature: temperature/100,
        tempo: tempo.value,
      });
      setOutputMidi(response.midiFile);
      setOutputMP3(response.mp3File);
      setOutputLoading(false);
    } catch (error) {
      setOutputLoading(false);
      setErrorMessage(error.message);
      console.log(error);
    }
  }
  return (
    <div className="App">
      <Collapse in={!!errorMessage} className='alert-container'>
        <Alert 
          severity="warning"
          action={
            <IconButton
              aria-label="close"
              color="inherit"
              size="small"
              onClick={() => {
                setErrorMessage('');
              }}
            >
              <CloseIcon fontSize="inherit" />
            </IconButton>
          }
          sx={{ mb: 2 }}
        >
          {errorMessage}
        </Alert>
      </Collapse>
      <Header />
      <SeedMusic 
        setSeedName={setSeedName}
        setNote={setNote}
        setMode={setMode}
        temperature={temperature}
        setTemperature={setTemperature}
        setTempo={setTempo}
        setErrorMessage={setErrorMessage}
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
        setErrorMessage={setErrorMessage}
      />
    </div>
  );
}

export default App;
