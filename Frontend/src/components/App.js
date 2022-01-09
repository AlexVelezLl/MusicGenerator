import logo from './logo.svg';
import './App.css';
import Header from './Header';
import SeedMusic from './seedMusic';
import OutputMusic from './outputMusic';

function App() {
  return (
    <div className="App">
      <Header />
      <SeedMusic />
      <div className="generate-music-container">

      </div>
      <OutputMusic />
    </div>
  );
}

export default App;
