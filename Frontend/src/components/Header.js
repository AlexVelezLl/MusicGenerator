import React from 'react';

import './Header.scss';
import logo from '../logo.png';

const Header = () => {
  return (
    <div className='header'>
      <div className='title'>
        MUSIC <br/> GENERATOR
      </div>
      <div className='icon'>
        <img src={logo} alt='Logo' />
      </div>
    </div>
  );
};

export default Header;
