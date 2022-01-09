import React from 'react';
import MelodyPlayer from '../shared/MelodyPlayer';

import './index.css';

const OutputMusic = () => {
  return (
    <section className='output-music'>
      <h2>Output music</h2>
      <div className='output-music-container'>
        <div className='output-music-options'>
          <button className='btn'>
            Download music
          </button>
        </div>
        <div className='output-music-player'>
          <MelodyPlayer />
        </div>
      </div>
    </section>
  );
};

export default OutputMusic;
