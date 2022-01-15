import React from 'react';
import { Bars } from 'react-loader-spinner';
import MelodyPlayer from '../shared/MelodyPlayer';

import './index.scss';

const OutputMusic = (props) => {
  const { outputMidi, outputMP3, outputLoading } = props;
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
          <button className='btn'>
            Download music
          </button>
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
