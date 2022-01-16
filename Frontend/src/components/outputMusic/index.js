import React, { useState } from 'react';
import { Bars } from 'react-loader-spinner';
import MelodyPlayer from '../shared/MelodyPlayer';

import './index.scss';
import icCaretDown from '../../assets/caret-down-solid.svg';

const OutputMusic = (props) => {
  const { outputMidi, outputMP3, outputLoading } = props;
  const [outputMenuOpen, setOutputMenuOpen] = useState(false);
  const handleOutputMenuClick = (e) => {
    setOutputMenuOpen(!outputMenuOpen);
    e.stopPropagation();
  }
  document.addEventListener('click', () => {
    if (outputMenuOpen) {
      setOutputMenuOpen(false);
    }
  });
  return (
    <section className='output-music'>
      <h2>Output music</h2>
      <div 
        className='output-music-container'
        style={{
          marginBottom: outputLoading ? '200px' : '0',
        }}
      >
        <div className='output-music-options'>
          <div className='dropdown-button'>
            <button 
              className='btn'
              onClick={handleOutputMenuClick}
              disabled={outputLoading || !outputMidi}
            >
              Download music <img src={icCaretDown} alt='caret-down' />
            </button>
            {
              outputMenuOpen &&
              <div className="dropdown-items">
                <div className="dropdown-item">
                  Donwload MIDI
                </div>
                <div className="dropdown-item">
                  Donwload MP3
                </div>
              </div>
            }
          </div>
        </div>
        <div className='output-music-player'>
        {
            outputLoading &&
            <div
              className="loader"
            >
              <h2>Cargando audio...</h2>
              <div style={{ marginLeft: "40px" }}>
                <Bars
                  color="#4CC678"
                  height={100}
                  width={100}
                  visible={outputLoading}
                />
              </div>
            </div>
          }
          {
            !outputLoading && 
            outputMP3 && 
            <MelodyPlayer audio={outputMP3} />
          }
        </div>
      </div>
    </section>
  );
};

export default OutputMusic;
