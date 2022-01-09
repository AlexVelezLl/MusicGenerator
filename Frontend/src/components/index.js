import React from 'react';
import './index.css';
import Header from './Header';
import SeedMusic from './seedMusic';
import OutputMusic from './outputMusic';

const App = () => {
  return (
    <div className="App">
      <Header />
      <SeedMusic />
      <div className="generate-music-container">
        <button className='btn'>
          GENERATE MUSIC
        </button>
      </div>
      <OutputMusic />
    </div>
  );
}

export default App;
